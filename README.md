# Temporal Content Analysis with TRIBE v2 and YouTube Analytics

This repository contains the IEEE Access manuscript source and compiled PDF,
publication figures, sanitized aggregate result tables, and a small script for
regenerating selected figures.

## Scope

The analysis treats each public video as the unit of study. TRIBE v2 outputs
are model-derived predictions from audiovisual content, not measurements of
viewers' brain activity, psychological state, learning, or military readiness.
The public files contain aggregate results only; video- and window-level
Analytics-derived records and private owner reports are excluded.

## Contents

- `main.pdf`, `main.tex`, `appendix.tex`, and `references.bib`: manuscript.
- `figures/`: publication figures; PDF files are used by the LaTeX source.
- `data/`: sanitized aggregate tables, configuration, and figure provenance.
- `build_review_figures.py`: regenerates selected figures from included
  aggregate tables. It does not run TRIBE v2 or collect YouTube data.
- IEEE Access and bibliography template assets required to compile the paper.

## Build

With a LaTeX distribution that includes the required packages, run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Data and Code Availability

The Zenodo versioned archive contains the figure-generation script,
configuration, checksums and provenance, selected aggregate result and audit
tables, and publication figures:

https://doi.org/10.5281/zenodo.22916779

The script regenerates four selected figures from released aggregates. The
archive does not reproduce the complete analysis from raw inputs, rerun TRIBE
v2 inference, or recollect owner-authorized YouTube Analytics reports. It
excludes raw media and Analytics responses, video- or window-level records,
credentials, model weights, runtime caches, and private owner records.
