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


def prediction_figure() -> Path:
    metrics = pd.read_csv(AUDIT / "fair_model_metrics.csv")
    ridge = metrics[metrics["family"].eq("ridge")].copy()
    feature_sets = ["metadata", "metadata_roi", "metadata_roi_changes"]
    labels = ["Metadata", "Metadata + ROI", "Metadata + ROI + change"]
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
        ax.set_xticks(np.arange(3), ["Meta", "+ ROI", "+ change"], rotation=35, ha="right", fontsize=7)
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
        ax.set_ylabel("Change" if ax is axes[0] else "")
        style(ax)
    return save(fig, "05_pattern_change_events.pdf")


def transfer_figure() -> Path:
    data = pd.read_csv(DATA / "cross_channel_transfer.csv")
    directions = [
        ("yugsa_to_kfn", "YugsaTV -> KFN"),
        ("kfn_to_yugsa", "KFN -> YugsaTV"),
    ]
    models = ["metadata", "metadata_roi"]
    labels = ["Metadata", "Metadata + ROI"]
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
    outputs = [prediction_figure(), event_figure(), transfer_figure()]
    provenance = {
        "generator": "paper/IEEE_access/build_review_figures.py",
        "inputs": [
            "data/submission_audit/fair_model_metrics.csv",
            "data/submission_audit/matched_pattern_change_control_summary.csv",
            "data/cross_channel_transfer.csv",
        ],
        "outputs": [{"path": str(path.relative_to(ROOT)), "sha256": sha256(path)} for path in outputs],
        "interpretation": {
            "prediction": "same-family Ridge feature-set comparison; lower MAE is better",
            "events": "event, matched control, and event-minus-control descriptive contrasts",
            "transfer": "held-out R2 boundary display with zero baseline",
        },
    }
    (DATA / "review_figure_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "outputs": [str(p) for p in outputs]}))


if __name__ == "__main__":
    main()
