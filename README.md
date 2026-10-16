# Temporal Content Analysis with TRIBE v2 and YouTube Analytics

This repository contains the manuscript and a bounded reproducibility package
for the IEEE Access study. The versioned Zenodo records are linked by the
concept DOI: https://doi.org/10.5281/zenodo.22890875.

## Scope

The study analyzes public military-video content at video and time-window
levels. TRIBE v2 outputs are model-derived cortical representations of the
audio-visual stimulus, not measurements of viewers' brains, psychological
states, learning, or military readiness.

## Contents

- `main.pdf`: compiled manuscript.
- `main.tex`, `appendix.tex`, `references.bib`: manuscript source.
- `figures/`: manuscript figures; Figure 1 also has an editable SVG source.
- `data/`: sanitized metadata, aggregate results, audit tables, and checksums.
- `build_review_figures.py`: regenerates Figures 5-7 from released aggregate
  audit tables.
- `REPRODUCIBILITY_NOTES.md`: exact reproduction scope and commands.
- `CITATION.cff`: citation metadata.

## Reproduction

Compile the manuscript from this directory with a LaTeX installation that
includes the bundled IEEE Access class and IEEE bibliography style:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

With Python 3, NumPy, pandas, and Matplotlib installed, regenerate Figures
5-7 from the sanitized aggregate audit tables:

```text
python build_review_figures.py
```

Other analysis tables and figures are included as released artifacts. This
package does not rerun TRIBE v2 inference, collect YouTube metadata, or
re-query owner-authorized YouTube Analytics reports.

## Data boundary

The archive excludes raw video and audio, raw YouTube Analytics responses,
OAuth credentials and access tokens, model weights, runtime caches, and other
private owner-authorized records. The public release is intended for
manuscript review and the reproduction activities stated above, not as a
complete end-to-end data-collection or model-inference environment.
