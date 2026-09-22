# IEEE Access Manuscript Handoff Guide

This directory is the cleaned source package for the current IEEE Access
manuscript draft. The package is intended for review, editing, and local PDF
recompilation.

## Current State

- `main.pdf` is the latest compiled manuscript.
- Current length: 16 pages.
- The latest manual compile sequence completed successfully on 2026-09-21.
- No unresolved citation or cross-reference warnings were detected.
- Author, affiliation, declaration, ethics, funding, data-availability, and
  biography placeholders still require author review before submission.

## Important Files

- `main.tex`: main English manuscript source.
- `appendix.tex`: integrated appendix and extended audit material.
- `references.bib`: BibTeX bibliography.
- `main.bbl`: generated bibliography used by the current PDF.
- `figures/*.pdf`: nine manuscript figures used by the main text or appendix.
- `figures/00_pipeline_overview.svg`: editable vector source for Figure 1.
- `data/`: aggregate analysis, provenance, and submission-audit files.
- `build_review_figures.py`: reproducibly rebuilds the corrected Figures 5--7
  from `data/submission_audit/` and `data/cross_channel_transfer.csv`.
- `REVISION_REPORT_KO.md`: itemized C01--C10/A01--A04 revision report.
- `OPEN_QUESTIONS_KO.md`: unresolved author/source questions that must not be
  filled by inference.
- `REPRODUCIBILITY_NOTES.md`: exact compile and figure-generation commands and
  source-to-output mapping.
- `reference_*.md`: bibliography evidence, search, change, and audit records.
- `PDF_QA.md`: PDF layout and verification record.
- `IEEE_ACCESS_SUBMISSION_REQUIREMENTS.md`: submission-regulation checklist.
- `*.cls`, `*.sty`, `*.bst`, font files, and logo assets: required IEEE Access
  template resources. Do not remove them if the manuscript must compile in a
  clean TeX environment.

## Recompile on Windows

Open PowerShell in this directory:

```powershell
cd C:\path\to\IEEE_access
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the full sequence above after changing `main.tex`, `appendix.tex`,
`references.bib`, or citation keys. The generated `.aux`, `.blg`, and `.log`
files are build diagnostics, not handoff inputs.

## Figure Scope

The manuscript compiles from the PDF figures in `figures/`. Figure 1 combines
representative complete 9:16 video frames with model-input, cortical-output,
retention, and review stages. The displayed frames are explanatory examples;
the numerical analysis is documented by the provenance and audit files.

`build_pipeline_figure.py` is retained as the figure-generation record, but it
expects private analysis data and staged media outside this handoff package.
It cannot regenerate Figure 1 from this ZIP alone. Do not rerun it unless the
external source paths and source hashes are available.

`build_review_figures.py` is self-contained with respect to the sanitized audit
CSVs staged in this package. It regenerates Figures 5--7 only; it does not run
TRIBE, access YouTube, or require private Analytics responses.

## Interpretation Boundary

TRIBE v2 outputs are model-derived predicted cortical-response descriptors.
They are not measured viewer BOLD/fMRI signals, psychological measurements,
learning outcomes, or individual evaluations. The manuscript uses them for
content-level descriptive analysis and exploratory audience-retention
comparison; causal and population-level claims should not be added without a
new study design.

## Deliberately Excluded Work Files

The handoff ZIP omits temporary PDF-rendering images, agent planning
metadata, the duplicated original template directory, raster figure previews,
and LaTeX build diagnostics (`.aux`, `.blg`, `.log`). These files remain in the sibling directory
`IEEE_access_work_archive_20260921` on the original workstation and are not
required for normal review or compilation.

No raw media, private Analytics responses, credentials, access tokens, model
weights, runtime caches, or Python environments are included.
