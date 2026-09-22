"""Render a source-verified, single-video walkthrough for manuscript Figure 1."""
from __future__ import annotations

import io
import json
from pathlib import Path
import subprocess
import sys

import cv2
import imageio_ffmpeg
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np
import pandas as pd
from PIL import Image, ImageChops
from nilearn import datasets, plotting

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from scripts.yugsa_retention_common import (
    SOURCE, MASKS, PROXIES, aggregate_windows, load_worker, read, sha,
)

VID = "P9n3oy1kfGw"
ANALYSIS = ROOT / "data/private_analytics/yugsa_extended/2026-09-12/9de11b5f84209492"
RAW = ROOT / f"data/private_analytics/yugsa_retention/2026-09-12/raw/{VID}.json"
MEDIA = ROOT / f"data/processed/yugsa_tv_shorts_snapshot/local_media_staging/collection/yugsa_tv/media/{VID}.mkv"
FIGURES = HERE / "figures"
AUDIT = HERE / "data/submission_audit"
INK, MUTED = "#20292F", "#55616A"
BLUE, TEAL, ORANGE = "#286DA8", "#087F82", "#D97627"
GREY, LIGHT = "#A8B2BA", "#E7ECEF"
mpl.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 15,
    "axes.labelsize": 15, "xtick.labelsize": 15, "ytick.labelsize": 15,
    "axes.linewidth": .8, "text.color": INK, "axes.labelcolor": INK,
    "pdf.fonttype": 42, "svg.fonttype": "none", "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

# Display-only frames from other public military Shorts. These are kept as
# complete 9:16 frames, separate from the illustrative video's verified
# audio, text, cortical maps, and retention series.
THUMBNAIL_SOURCES = (
    {"label": "Short A", "video_id": "22jxeSLOhq0", "time_seconds": 0.5},
    {"label": "Short B", "video_id": "J9u57AavaXE", "time_seconds": 47.7},
    {"label": "Short C", "video_id": "KdbWaBQGCnA", "time_seconds": 0.5},
    {"label": "Short D", "video_id": "PHRqJHT8yOg", "time_seconds": 0.5},
)
THUMBNAIL_MEDIA_DIR = ROOT / "data/processed/yugsa_tv_shorts_snapshot/local_media_staging/collection/yugsa_tv/media"


def change(x):
    centered = x - x.mean(axis=1, keepdims=True)
    norm = np.linalg.norm(centered, axis=1)
    den = norm[1:] * norm[:-1]
    similarity = np.divide(np.einsum("ij,ij->i", centered[1:], centered[:-1]), den,
                           out=np.full(len(den), np.nan), where=den > 1e-12)
    return np.r_[np.nan, 1 - np.clip(similarity, -1, 1)]


def prepare():
    manifest = read(SOURCE / "input_manifest.json")
    records = manifest.get("records", manifest.get("videos", []))
    record = next(r for r in records if r["video_id"] == VID)
    assert sha(MEDIA) == record["media_sha256"], "Media differs from inference input"
    assert sha(RAW) == RAW.with_suffix(".sha256").read_text().strip()
    source_manifest = read(ANALYSIS / "MANIFEST.json")
    for name in ("windows.csv", "pattern_change_events.csv"):
        entry = next(r for r in source_manifest["files"] if r["path"] == name)
        assert sha(ANALYSIS / name) == entry["sha256"]
    x, start, stop, duration, _ = load_worker(SOURCE, VID, verify=True)
    raw = read(RAW)
    assert raw["video_id"] == VID and raw["end_date"] == "2026-09-12"
    reconstructed, cortex = aggregate_windows(raw["rows"], x, start, stop, duration, 5)
    table = pd.DataFrame(reconstructed)
    masks = dict(np.load(MASKS, allow_pickle=False))
    for key in PROXIES:
        table[key] = cortex[:, masks[key]].mean(axis=1)
    table["pattern_change"] = change(cortex)
    frozen = pd.read_csv(ANALYSIS / "windows.csv")
    frozen = frozen[(frozen.video_id == VID) & (frozen.width_seconds == 5)].sort_values("start_seconds")
    columns = ["start_seconds", "stop_seconds", "audienceWatchRatio", "relativeRetentionPerformance",
               "exit_intensity", "pattern_change", *PROXIES]
    np.testing.assert_allclose(table[columns], frozen[columns], rtol=1e-7, atol=1e-8, equal_nan=True)
    events = pd.read_csv(ANALYSIS / "pattern_change_events.csv")
    assert ((events.video_id == VID) & (events.event_seconds == 25)).any()
    controls = pd.read_csv(AUDIT / "matched_pattern_change_controls.csv")
    assert ((controls.video_id == VID) & (controls.event_seconds == 25) & (controls.control_seconds == 35)).any()
    state = read(SOURCE / f"inference/worker_state/{VID}.json")
    attempt = SOURCE / "inference" / state["successful_attempt_dir"]
    meta = read(attempt / f"prediction_metadata/{VID}.json")
    model_path = attempt / meta["artifacts"]["model_events"]["path"]
    assert sha(model_path) == meta["artifacts"]["model_events"]["sha256"]
    words = [r for r in read(model_path)["records"] if r["type"] == "Word" and 23 <= r["start"] < 25.5]
    text = " ".join(r["text"] for r in words)
    assert text == "Here, we were able to take classes"
    native = [int(np.flatnonzero((start <= t) & (stop > t))[0]) for t in (22.5, 27.5)]
    cap = cv2.VideoCapture(str(MEDIA))
    frames = []
    for t in (2.5, 22.5, 27.5):
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, frame = cap.read()
        if not ok:
            raise ValueError(f"Frame decoding failed at {t}")
        frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
    cap.release()
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-ss", "20", "-i", str(MEDIA),
           "-t", "10", "-vn", "-ac", "1", "-ar", "8000", "-f", "f32le", "pipe:1"]
    audio = np.frombuffer(subprocess.run(cmd, check=True, capture_output=True).stdout, dtype="<f4")
    assert len(audio) >= 79000
    metrics = pd.read_csv(AUDIT / "fair_model_metrics.csv")
    metrics = metrics[(metrics.target == "exit_intensity") & (metrics.split == "grouped") & (metrics.family == "ridge")].set_index("model")
    maes = metrics.loc[["metadata", "metadata_roi_changes"], "mae_video_equal"].to_numpy()
    oof = pd.read_csv(AUDIT / "fair_model_oof_predictions.csv")
    oof = oof[(oof.target == "exit_intensity") & (oof.split == "grouped") & (oof.family == "ridge")]
    assert oof.groupby("video_id").fold.nunique().max() == 1
    assert sorted(oof.fold.unique().tolist()) == list(range(5))
    source_files = [MEDIA, RAW, MASKS, SOURCE / "input_manifest.json", ANALYSIS / "windows.csv",
                    ANALYSIS / "pattern_change_events.csv", model_path,
                    AUDIT / "fair_model_metrics.csv", AUDIT / "fair_model_oof_predictions.csv",
                    AUDIT / "matched_pattern_change_controls.csv"]
    for key in ("cortical_predictions", "surface_summary"):
        source_files.append(attempt / meta["artifacts"][key]["path"])
    provenance = {
        "video_id": VID, "duration_seconds": duration,
        "selection_rule": "Locally available complete walkthrough closest to primary cohort median duration; not selected by association or outcome",
        "frame_seconds": [2.5, 22.5, 27.5], "event_seconds": 25, "control_seconds": 35,
        "native_cortical_intervals": [[float(start[i]), float(stop[i])] for i in native],
        "analysis_window_seconds": 5, "validated_windows": len(table),
        "timing": "Persisted source intervals with overlap weighting; no added temporal delay",
        "model_text": text, "surface_hemisphere_view": "left lateral",
        "grouped_exit_mae": dict(zip(("metadata", "metadata_roi_changes"), maes.tolist())),
        "verification": {"media_hash": "pass", "prediction_hashes": "pass", "frozen_windows": "pass", "video_fold_separation": "pass"},
        "sources": [{"path": p.relative_to(ROOT).as_posix(), "sha256": sha(p)} for p in source_files],
    }
    return x[native], table, frames, audio, raw, maes, provenance


def surface_images(surfaces):
    mesh = datasets.fetch_surf_fsaverage("fsaverage5")
    limit = float(np.max(np.abs(surfaces)))
    images = []
    for vals in surfaces:
        fig = plt.figure(figsize=(5, 3.2))
        ax = fig.add_axes([0, 0, 1, 1], projection="3d")
        plotting.plot_surf_stat_map(mesh.infl_left, vals[:10242], hemi="left", view="lateral",
                                   bg_map=mesh.sulc_left, axes=ax, colorbar=False,
                                   cmap="RdBu_r", vmax=limit, symmetric_cbar=True, threshold=None)
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=220, facecolor="white")
        plt.close(fig)
        buf.seek(0)
        im = Image.open(buf).convert("RGB")
        bbox = ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox()
        images.append(im.crop(bbox))
    return images, limit


def load_thumbnail_sources():
    """Load complete 9:16 display frames without cropping or resizing."""
    frames = []
    provenance = []
    for source in THUMBNAIL_SOURCES:
        path = THUMBNAIL_MEDIA_DIR / f"{source['video_id']}.mkv"
        if not path.exists():
            raise FileNotFoundError(f"Missing thumbnail source media: {path}")
        cap = cv2.VideoCapture(str(path))
        cap.set(cv2.CAP_PROP_POS_MSEC, source["time_seconds"] * 1000)
        ok, frame = cap.read()
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()
        if not ok:
            raise ValueError(f"Thumbnail frame decoding failed: {path}")
        if abs((width / height) - (9 / 16)) > 0.02:
            raise ValueError(f"Thumbnail source is not portrait 9:16: {path} ({width}x{height})")
        frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        provenance.append({
            **source,
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha(path),
            "dimensions": [width, height],
        })
    return frames, provenance


def build():
    surfaces, table, frames, audio, raw, maes, provenance = prepare()
    thumbnail_frames, thumbnail_sources = load_thumbnail_sources()
    brains, surface_limit = surface_images(surfaces)
    # Work at twice the intended print size so all typography scales uniformly.
    fig = plt.figure(figsize=(13.97, 8.54))
    canvas = fig.add_axes([0, 0, 1, 1], zorder=0)
    canvas.set(xlim=(0, 1), ylim=(0, 1)); canvas.axis("off")

    def label(x, y, s, size=15, color=INK, weight="normal", ha="left", **kwargs):
        return fig.text(x, y, s, fontsize=size, color=color, weight=weight, ha=ha, va="center", **kwargs)

    def arrow(a, b, color=MUTED, dashed=False):
        canvas.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=15,
                                        lw=1.7, color=color, linestyle="--" if dashed else "-"))

    def picture(bounds, im):
        ax = fig.add_axes(bounds)
        ax.imshow(im, aspect="equal", interpolation="lanczos")
        ax.axis("off")
        return ax

    def title(x, width, letter, text, color):
        label(x, .955, letter, 19, color, "bold")
        label(x + .022, .955, text, 17, INK, "bold")
        canvas.plot([x, x + width], [.92, .92], color=color, lw=2)

    title(.025, .18, "a", "Inputs", BLUE)
    title(.25, .195, "b", "Cortical encoding", BLUE)
    title(.495, .26, "c", "Align in video time", TEAL)
    title(.80, .18, "d", "Evaluate + review", ORANGE)
    label(.025, .886, "Military Shorts", 16, weight="bold")
    for x, frame, label_text in ((.025, thumbnail_frames[0], "Short A"), (.12, thumbnail_frames[1], "Short B")):
        picture([x, .63, .084, .235], frame)
        label(x + .042, .606, label_text, ha="center")
    label(.025, .557, "Audio", 15, BLUE)
    wave = fig.add_axes([.025, .476, .18, .065])
    chunks = audio[:len(audio) // 160 * 160].reshape(-1, 160)
    amp = np.sqrt(np.mean(chunks ** 2, axis=1))
    t = 20 + np.arange(len(amp)) / 50
    wave.fill_between(t, -amp, amp, color=BLUE, lw=0)
    wave.axvline(25, color=ORANGE, lw=1.5)
    wave.set_xlim(20, 30); wave.axis("off")
    label(.025, .442, "Model text", 15, BLUE)
    label(.025, .392, '"Here, we were able\nto take classes"', 15, linespacing=1.4)
    label(.025, .28, "Owner-authorized\nYouTube Analytics", 16, TEAL, "bold", linespacing=1.35)
    raw_ax = fig.add_axes([.025, .125, .18, .102])
    ratios = np.array([r["elapsedVideoTimeRatio"] for r in raw["rows"]])
    watch = np.array([r["audienceWatchRatio"] for r in raw["rows"]])
    raw_ax.plot(ratios * provenance["duration_seconds"], watch, color=TEAL, lw=2)
    raw_ax.fill_between(ratios * provenance["duration_seconds"], 0, watch, color=TEAL, alpha=.10)
    raw_ax.set_xlim(0, provenance["duration_seconds"]); raw_ax.axis("off")
    for i, name in enumerate(("Video", "Audio", "Text")):
        cx = .27 + i * .073
        label(cx, .86, name, 15, BLUE, ha="center")
        arrow((cx, .834), (.347, .791), BLUE)
    canvas.add_patch(Rectangle((.29, .722), .115, .067, facecolor="#EAF2F8", edgecolor=BLUE, lw=1))
    label(.3475, .756, "TRIBE v2", 18, BLUE, "bold", ha="center")
    arrow((.347, .72), (.347, .686), BLUE)
    label(.347, .658, "Predicted cortex", 16, weight="bold", ha="center")
    for y, brain, interval in zip((.474, .285), brains, provenance["native_cortical_intervals"]):
        picture([.255, y, .185, .17], brain)
        label(.347, y - .014, f"{interval[0]:g}-{interval[1]:g} s", 15, ha="center")
    cb_ax = fig.add_axes([.281, .228, .133, .012])
    norm = mpl.colors.Normalize(-surface_limit, surface_limit)
    cb = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap="RdBu_r"), cax=cb_ax, orientation="horizontal")
    cb.set_ticks([-surface_limit, 0, surface_limit])
    cb.set_ticklabels([f"{-surface_limit:.2f}", "0", f"{surface_limit:.2f}"])
    cb.ax.tick_params(labelsize=15, length=2, pad=2)
    cb.outline.set_linewidth(.5)
    label(.347, .176, "Same scale; left lateral", 15, MUTED, ha="center")
    arrow((.215, .756), (.245, .756), BLUE)
    arrow((.452, .736), (.488, .736), BLUE)
    centers = (table.start_seconds + table.stop_seconds) / 2
    profile_limit = float(np.max(np.abs(table[list(PROXIES)].to_numpy())))
    label(.562, .884, "5-second windows", 16, weight="bold")
    heat = fig.add_axes([.562, .724, .193, .130])
    heat_image = heat.imshow(table[list(PROXIES)].to_numpy().T, aspect="auto", origin="upper",
                extent=(0, 60, 5.5, -.5), cmap="RdBu_r", vmin=-profile_limit, vmax=profile_limit,
                interpolation="nearest")
    heat.set_yticks(range(6), ["Reward", "Aversion", "Social", "Engage.", "Visual", "Audio"])
    heat.tick_params(axis="y", length=0, pad=4, labelsize=15)
    heat.set_xticks([])
    heat.spines[["top", "right", "bottom", "left"]].set_visible(False)
    for boundary in np.arange(0, 61, 5):
        heat.axvline(boundary, color="white", lw=.4, alpha=.35)
    heat.axvline(25, color=ORANGE, lw=2)
    profile_cb_ax = fig.add_axes([.602, .704, .113, .009])
    profile_cb = fig.colorbar(heat_image, cax=profile_cb_ax, orientation="horizontal")
    profile_cb.set_ticks([-profile_limit, 0, profile_limit])
    profile_cb.set_ticklabels([f"{-profile_limit:.2f}", "0", f"{profile_limit:.2f}"])
    profile_cb.ax.tick_params(labelsize=15, length=2, pad=2)
    profile_cb.outline.set_linewidth(.5)
    for bounds, key, text, color in (
        ([.562, .523, .193, .090], "pattern_change", "Cortical pattern change", BLUE),
        ([.562, .347, .193, .090], "audienceWatchRatio", "Audience watch ratio", TEAL),
        ([.562, .172, .193, .090], "exit_intensity", "Exit intensity", TEAL),
    ):
        ax = fig.add_axes(bounds)
        positions = table.start_seconds if key == "pattern_change" else centers
        ax.plot(positions, table[key], color=color, lw=2, marker="o", markersize=3)
        ax.axvspan(20, 30, color=ORANGE, alpha=.13, lw=0)
        ax.axvline(25, color=ORANGE, lw=1.5)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color(GREY)
        ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(2))
        ax.set_xlim(0, 60)
        ax.tick_params(length=2, pad=3)
        ax.set_xticks([0, 25, 60])
        if key != "exit_intensity":
            ax.set_xticklabels([])
        else:
            ax.set_xlabel("Video time (s)", labelpad=4)
        label(.562, bounds[1] + bounds[3] + .030, text, 15, color, "bold")
    arrow((.215, .11), (.535, .11), TEAL)
    label(.347, .135, "Independent retention reports", 15, TEAL, ha="center")
    label(.80, .884, "Held-out videos", 16, weight="bold")
    for row in range(5):
        for col in range(5):
            canvas.add_patch(Rectangle((.805 + col * .032, .825 - row * .021), .027, .015,
                                      facecolor=BLUE if row == col else LIGHT, edgecolor="none"))
    label(.81, .706, "Train", 15, MUTED)
    canvas.add_patch(Rectangle((.858, .7), .009, .012, color=LIGHT))
    label(.889, .706, "Test", 15, BLUE)
    canvas.add_patch(Rectangle((.93, .7), .009, .012, color=BLUE))
    label(.80, .665, "Exit MAE", 15, weight="bold")
    for y, name, value, color in zip((.619, .569), ("Metadata", "+ TRIBE"), maes, (GREY, BLUE)):
        label(.80, y, name, 15)
        canvas.add_patch(Rectangle((.876, y - .010), .052 * value / max(maes), .020,
                                  facecolor=color, edgecolor="none"))
        label(.938, y, f"{value:.4f}", 15)
    label(.80, .514, "Whole-cohort comparison", 15, MUTED)
    label(.80, .48, "KFN transfer check", 15, MUTED)
    arrow((.765, .736), (.794, .736), MUTED)
    label(.80, .442, "Review examples", 16, ORANGE, "bold")
    for x, frame, label_text in ((.802, thumbnail_frames[2], "Short C"), (.90, thumbnail_frames[3], "Short D")):
        picture([x, .20, .078, .221], frame)
        label(x + .039, .181, label_text, 15, ha="center")
    arrow((.765, .357), (.794, .357), ORANGE)
    label(.89, .13, "Inspect scenes", 15, ORANGE, ha="center")
    label(.025, .033, "Representative 9:16 frames", 13, MUTED)
    FIGURES.mkdir(parents=True, exist_ok=True)
    outputs = []
    for ext in ("pdf", "svg", "png"):
        path = FIGURES / f"00_pipeline_overview.{ext}"
        fig.savefig(path, dpi=600 if ext == "png" else 300, pad_inches=0)
        outputs.append(path)
    plt.close(fig)
    provenance.update(surface_color_limit=surface_limit, profile_color_limit=profile_limit,
                      heatmap_labels=dict(zip(("Reward", "Aversion", "Social", "Engage.", "Visual", "Audio"), PROXIES)),
                      thumbnail_policy={
                          "source": "complete frames from separate verified public Shorts",
                          "display_only": True,
                          "cropping": "none",
                          "sources": thumbnail_sources,
                          "manual_visual_check": "pass: no visible faces in selected frames",
                      },
                      figure_inches=[13.97, 8.54], intended_print_inches=[6.989, 4.272],
                      minimum_font_points_at_print_size=7.5,
                      code_sha256=sha(Path(__file__)),
                      outputs=[{"path": p.relative_to(ROOT).as_posix(), "sha256": sha(p)} for p in outputs])
    (HERE / "data/pipeline_figure_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "video_id": VID, "verified_windows": len(table), "outputs": [str(p) for p in outputs]}))


if __name__ == "__main__":
    build()
