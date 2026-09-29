# Temporal Content Analysis with TRIBE v2 and YouTube Analytics

This repository provides the IEEE Access manuscript source, compiled PDF,
publication figures, selected figure-regeneration code, and sanitized aggregate
result tables.

## Scope

The unit of analysis is public video content. TRIBE v2 outputs are model-derived
cortical predictions, not measurements of viewers' brain activity,
psychological state, learning, or military readiness. This repository contains
aggregate results only; video- and window-level YouTube Analytics records and
private owner reports are not distributed.

## Contents

- `main.pdf`, `main.tex`, `appendix.tex`, and `references.bib`: the manuscript.
- `figures/`: publication-ready figures used by the LaTeX source.
- `data/`: sanitized aggregate result tables, configuration, and provenance.
- `build_review_figures.py`: regenerates selected figures from the included
  aggregates; it does not collect YouTube data or run TRIBE v2.
- IEEE Access and bibliography template assets required to build the PDF.

## Build

Run from this directory with a LaTeX distribution that includes the required
packages:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Data Availability

The associated Zenodo deposit is version 1.0.2, a data-only archive containing
a README and sanitized aggregate data files. The concept DOI resolves to the
latest version:

https://doi.org/10.5281/zenodo.22916778

The Zenodo archive does not contain code or pre-rendered figures. The public
GitHub repository provides the manuscript source, selected figure-generation
code, figures, and aggregate tables. The public materials do not reproduce the
full analysis from raw inputs, rerun TRIBE v2 inference, or recollect
owner-authorized YouTube Analytics reports. Raw media, raw Analytics responses,
video- or window-level records, credentials, model weights, runtime caches, and
private owner records are excluded.
