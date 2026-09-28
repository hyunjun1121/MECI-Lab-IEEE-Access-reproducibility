"""Build the corrected review figures from the sanitized submission audit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
AUDIT = DATA / "submission_audit"
FIGURES = ROOT / "figures"

BLUE = "#1f5a94"
TEAL = "#168a8a"
ORANGE = "#d97904"
GRAY = "#6f7782"
INK = "#1d2630"
LIGHT = "#d8dee6"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def style(ax: plt.Axes) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines["left"].set_color(LIGHT)
    ax.spines["bottom"].set_color(LIGHT)
    ax.grid(axis="y", color=LIGHT, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, labelsize=8)


def save(fig: plt.Figure, name: str) -> Path:
    path = FIGURES / name
    fig.savefig(path, format="pdf", bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    return path


def association_figure() -> Path:
    summary = pd.read_csv(AUDIT / "position_adjusted_circular_shift_summary.csv")
    features = [
        "reward", "aversion", "social_value", "engagement",
        "visual_processing", "auditory_processing", "pattern_change", "amplitude_change",
    ]
    labels = {
        "reward": "Frontal profile",
        "aversion": "Anterior-insular profile",
        "social_value": "Cingulo-parietal profile",
        "engagement": "Posterior-cingulate profile",
        "visual_processing": "Visual-cortical profile",
        "auditory_processing": "Auditory-cortical profile",
        "pattern_change": "Cortical pattern change",
        "amplitude_change": "Mean absolute cortical change",
    }
    targets = [
        ("audienceWatchRatio", "Audience watch ratio"),
        ("relativeRetentionPerformance", "Relative retention"),
        ("exit_intensity", "Exit intensity"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(7.1, 3.65), sharey=True,
                             gridspec_kw={"wspace": 0.20})
    y = np.arange(len(features))
    for ax, (target, title) in zip(axes, targets):
        data = summary[summary["target"].eq(target)].set_index("feature").loc[features]
        means = data["observed_mean_rho"].to_numpy(float)
        low = data["observed_bootstrap_low"].to_numpy(float)
        high = data["observed_bootstrap_high"].to_numpy(float)
        ax.errorbar(means, y, xerr=np.vstack((means - low, high - means)),
                    fmt="o", color=BLUE, ecolor=BLUE, elinewidth=1.1,
                    capsize=2.2, markersize=3.4)
        ax.axvline(0, color=INK, linewidth=0.7)
        ax.set_title(title, fontsize=8, color=INK, weight="bold", pad=5)
        ax.set_xlim(-0.2, 0.6)
        ax.set_xticks([-0.2, 0.0, 0.2, 0.4, 0.6])
        ax.set_ylim(len(features) - 0.5, -0.5)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color(LIGHT)
        ax.xaxis.grid(color=LIGHT, linewidth=0.6, alpha=0.7)
        ax.set_axisbelow(True)
        ax.tick_params(length=0, labelsize=7)
    axes[0].set_yticks(y, [labels[key] for key in features], fontsize=7)
    for ax in axes[1:]:
        ax.tick_params(labelleft=False)
    fig.supxlabel("Mean within-video Spearman correlation (ρ)", fontsize=8, y=0.045)
    fig.subplots_adjust(left=0.30, right=0.99, bottom=0.18, top=0.84)
    return save(fig, "01_continuous_associations.pdf")


def prediction_figure() -> Path:
    metrics = pd.read_csv(AUDIT / "fair_model_metrics.csv")
    ridge = metrics[metrics["family"].eq("ridge")].copy()
    feature_sets = ["metadata", "metadata_roi", "metadata_roi_changes"]
    labels = ["Metadata", "Metadata + profiles", "Metadata + profiles + changes"]
    targets = [
        ("audienceWatchRatio", "Watch ratio"),
        ("relativeRetentionPerformance", "Relative retention"),
        ("exit_intensity", "Exit intensity"),
    ]
    colors = [GRAY, TEAL, BLUE]
    fig, axes = plt.subplots(1, 4, figsize=(7.2, 3.05), gridspec_kw={"wspace": 0.42})
    for ax, (target, title), split in [
        (axes[0], targets[0], "grouped"),
        (axes[1], targets[1], "grouped"),
        (axes[2], targets[2], "grouped"),
        (axes[3], targets[2], "chronological"),
    ]:
        subset = ridge[(ridge["target"].eq(target)) & (ridge["split"].eq(split))]
        values = [float(subset.loc[subset["model"].eq(model), "mae_video_equal"].iloc[0]) for model in feature_sets]
        bars = ax.bar(np.arange(3), values, color=colors, width=0.68)
        ax.set_title(("Grouped\n" if split == "grouped" else "Chronological\n") + title, fontsize=8.5, color=INK, weight="bold", pad=4)
        ax.set_xticks(np.arange(3), ["Meta", "+ profiles", "+ changes"], rotation=35, ha="right", fontsize=7)
        ax.set_ylabel("MAE" if ax is axes[0] else "")
        ax.set_ylim(0, max(values) * 1.28)
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, value + max(values) * 0.035, f"{value:.4f}", ha="center", va="bottom", fontsize=6.8, rotation=90)
        style(ax)
    return save(fig, "02_predictive_increment.pdf")


def event_figure() -> Path:
    summary = pd.read_csv(AUDIT / "matched_pattern_change_control_summary.csv").set_index("target")
    panels = [
        ("audienceWatchRatio", "Audience watch ratio", BLUE),
        ("exit_intensity", "Exit intensity", TEAL),
        ("relativeRetentionPerformance", "Relative retention", ORANGE),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(7.1, 2.55), gridspec_kw={"wspace": 0.48})
    for ax, (target, title, color) in zip(axes, panels):
        row = summary.loc[target]
        means = [row.event_mean, row.control_mean, row.difference_in_differences_mean]
        lows = [row.event_bootstrap_low, row.control_bootstrap_low, row.difference_in_differences_low]
        highs = [row.event_bootstrap_high, row.control_bootstrap_high, row.difference_in_differences_high]
        yerr = np.vstack([np.asarray(means) - np.asarray(lows), np.asarray(highs) - np.asarray(means)])
        positions = np.arange(3)
        ax.errorbar(positions, means, yerr=yerr, fmt="o", color=color, ecolor=color, elinewidth=1.5, capsize=3, markersize=5)
        ax.axhline(0, color=INK, linewidth=0.8)
        ax.set_xticks(positions, ["Event", "Control", "Event -\ncontrol"], fontsize=7)
        ax.set_title(title, fontsize=8.7, color=INK, weight="bold", pad=4)
        ax.set_ylabel("After - before" if ax is axes[0] else "")
        style(ax)
    return save(fig, "05_pattern_change_events.pdf")


def transfer_figure() -> Path:
    data = pd.read_csv(DATA / "cross_channel_transfer.csv")
    directions = [
        ("yugsa_to_kfn", "YugsaTV -> KFN"),
        ("kfn_to_yugsa", "KFN -> YugsaTV"),
    ]
    models = ["metadata", "metadata_roi"]
    labels = ["Metadata", "Metadata + profiles"]
    colors = [GRAY, BLUE]
    fig, axes = plt.subplots(1, 2, figsize=(6.2, 2.55), sharey=True, gridspec_kw={"wspace": 0.25})
    for ax, (direction, title) in zip(axes, directions):
        subset = data[data["direction"].eq(direction)].set_index("model")
        values = [float(subset.loc[model, "r2"]) for model in models]
        bars = ax.bar(np.arange(2), values, color=colors, width=0.58)
        ax.axhline(0, color=INK, linewidth=0.8)
        ax.set_title(title, fontsize=8.8, color=INK, weight="bold", pad=4)
        ax.set_xticks(np.arange(2), labels, rotation=25, ha="right", fontsize=7)
        ax.set_ylabel("Held-out $R^2$" if ax is axes[0] else "")
        ax.set_ylim(-1.6, 0.15)
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, value - 0.07, f"{value:.3f}", ha="center", va="top", fontsize=7, color="white", weight="bold")
        style(ax)
    return save(fig, "03_cross_channel.pdf")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    outputs = [association_figure(), prediction_figure(), event_figure(), transfer_figure()]
    provenance = {
        "generator": "build_review_figures.py",
        "inputs": [
            "data/submission_audit/fair_model_metrics.csv",
            "data/submission_audit/matched_pattern_change_control_summary.csv",
            "data/submission_audit/position_adjusted_circular_shift_summary.csv",
            "data/cross_channel_transfer.csv",
        ],
        "outputs": [{"path": str(path.relative_to(ROOT)), "sha256": sha256(path)} for path in outputs],
        "interpretation": {
            "prediction": "same-family Ridge feature-set comparison; lower MAE is better",
            "associations": "position-adjusted within-video correlations with 95% video-bootstrap intervals",
            "events": "event, matched control, and event-minus-control descriptive contrasts",
            "transfer": "held-out R2 boundary display with zero baseline",
        },
    }
    (DATA / "review_figure_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "outputs": [str(p) for p in outputs]}))


if __name__ == "__main__":
    main()
