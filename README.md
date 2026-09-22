# Temporal Content Analysis with TRIBE v2 and Owner-Authorized YouTube Analytics

This repository is the reproducibility companion for the IEEE Access manuscript
`Temporal Content Analysis with TRIBE v2 and Owner-Authorized YouTube Analytics`.
It contains the manuscript source and PDF, sanitized aggregate data, figures,
configuration records, and audit outputs used to prepare the article.

## Scope

The study analyzes public military-video content at the video and time-window
levels. TRIBE v2 outputs are model-derived cortical representations of the
audiovisual stimulus. They are not measurements of viewer brain activity,
psychological state, learning, or military readiness.

## Contents

- `main.pdf`: compiled manuscript.
- `main.tex`, `appendix.tex`, `references.bib`: manuscript source.
- `figures/`: manuscript figures and editable Figure 1 sources.
- `data/`: sanitized aggregate tables, analysis summaries, configurations,
  provenance, and submission-audit outputs.
- `HANDOFF_GUIDE.md`, `REPRODUCIBILITY_NOTES.md`: reproduction boundaries and
  source-to-result documentation.
- `CITATION.cff`: citation metadata for this archive.

## Reproduction

The manuscript can be rebuilt from this directory with:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The package is intended to reproduce the manuscript and its aggregate displays;
it does not rerun TRIBE v2 inference or YouTube collection.

## Data-sharing boundary

The archive contains sanitized public metadata, derived aggregate results,
figures, configuration, manifests, and checksums. It intentionally excludes
raw video and audio, raw owner-authorized YouTube Analytics responses, OAuth
credentials, access tokens, model weights, runtime caches, and private records.
The public Zenodo DOI for the versioned release will be added to the manuscript
Data Availability statement after the GitHub release is archived.

## Citation

Please cite the versioned Zenodo record after its DOI is assigned. The author
order and affiliation metadata are provided in `CITATION.cff`.

## Contact

Corresponding author: Hyun-Myung Lim, Korea Military Academy,
`onlybyhim@kma.ac.kr`.
