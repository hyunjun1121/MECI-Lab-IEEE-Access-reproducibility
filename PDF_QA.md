# IEEE Access PDF QA

Checked: 2026-09-22

## Build

Working directory: `paper/IEEE_access/`

The local MiKTeX installation does not provide the Perl runtime required by
`latexmk`. The PDF was therefore built with the equivalent manual sequence:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Result: `main.pdf`, 15 pages, 2,040,258 bytes after the 2026-09-22
bibliography-integrity cleanup.
Figures 1--7 are the main reader-facing sequence. Figure 8 is an integrated
Appendix composite containing the two extended descriptive analyses. Tables
1--7 and the full Appendix are included in the same PDF. The final LaTeX pass
has no unresolved citations or cross-references.

The reference audit also passes: 45 cited keys, 45 BibTeX entries, no unused
or missing keys, no duplicate DOI, no placeholder metadata, and complete
coverage in `reference_evidence_matrix.md`. The bibliography was rebuilt with
BibTeX after the source additions and the two final `pdflatex` passes.

The manuscript is deliberately below the IEEE Access strongly recommended
20-page length. It includes the workflow, primary results, robustness audits,
extended descriptive analyses, and reproducibility record without padding the
paper with duplicate plots or raw-output inventory.

## Visual review

Figure 1 was rebuilt on 2026-09-22 as a left-to-right single-video walkthrough.
The input-panel label was shortened to `Military Shorts` so it does not enter
the adjacent cortical-encoding column.
Actual source frames, a measured audio envelope, persisted model-input text,
two predicted cortical surfaces, and aligned retention traces replace the old
miniature result-chart montage. The staged media hash matches the inference
input manifest. All 12 five-second example windows reproduce the frozen
analysis table; the 25-second event and 35-second matched control are verified.
Grouped evaluation keeps each video's windows in one fold. These checks and
source/output hashes are in `data/pipeline_figure_provenance.json`.

The revised standalone figure and manuscript Figure 1 on page 3 were inspected
visually. The minimum figure label size at the template's full text width is
approximately 7.5 pt. PDF and SVG preserve vector labels and curves; the PNG
is 600 dpi. The whole manuscript was rendered at 110 dpi for layout review,
with the changed end pages inspected after float adjustments. A `\clearpage`
after the Appendix flushes all pending Appendix tables and figures before the
declarations, and a second `\clearpage` starts the reference list on its own
page. No unresolved references remain. The revision introduced no visible
clipping or collisions. Author placeholders and the previously documented
template font warnings remain.

### Final end-page review (2026-09-21)

The final PDF was rendered with MiKTeX Poppler `pdftoppm` at 120 dpi into
`tmp/pdf_qa/review_20260921_final/` and inspected page by page with the image viewer.
The review found:

- no clipped text, table rows, captions, or figure edges;
- no overlapping figures, tables, captions, headers, or footers;
- readable figure and table labels at the compiled PDF scale, including the
  full-width workflow overview on page 3;
- stable IEEE Access two-column layout and page numbering;
- Appendix figures and tables finish before the declaration sections;
- the reference list starts on a new page and contains no interleaved figures;
- the author biography follows the reference list;
- the composite Figure 8 keeps both extended plots legible without collision.

Page 10 ends the conclusion before the deliberate Appendix page break; pages
10--12 contain the Appendix material, page 13 contains declarations, and pages
14--15 contain the reference list followed by the author biography. The blank
lower area on page 13 is intentional declaration/page-break whitespace,
not a collision or missing object. The reference list is deliberately kept
separate from figures and tables.

### Declaration-page spacing review (2026-09-22)

The declaration page was re-rendered after applying local `\\raggedbottom`
spacing and an explicit column break before Acknowledgment. Data Availability
and Ethics and Governance now occupy the left column, Acknowledgment occupies
the right column without splitting, and the reference list begins on page 14.
No heading-to-paragraph stretch, column interruption, clipping, or overlap was
observed.

The revised review-driven figures were checked for readability and clipping:
Figure 5 uses same-family Ridge MAE comparisons, Figure 6 uses matched
event/control five-second windows, and Figure 7 uses held-out cross-channel R2
with an explicit zero baseline. No unresolved citation or cross-reference
markers were visible.

### Figure-text simplification review (2026-09-22)

The standalone Figure 5--7 PDFs and manuscript pages 3, 8, and 9 were
re-rendered after removing prose that duplicated the captions or main text.
Figure 5 no longer carries a global evaluation sentence or a bottom
interpretive note; Figure 6 no longer carries the sample-size and bootstrap
notes inside the plot; Figure 7 no longer carries the transfer-boundary title,
training/testing counts, or the negative-$R^2$ explanation inside the plot.
Figure 1 no longer repeats its example-video note at the bottom. Panel titles,
axis labels, legends, plotted values, and pipeline-stage labels remain. The
removed sample sizes and interpretation remain in the corresponding captions
and manuscript text. No clipping, overlap, or unreadable labels were observed.

### Reference integrity cleanup (2026-09-22)

The manuscript no longer cites the separate Google OAuth implementation page.
The study-provenance sentence now states only that the channel owner authorized
read-only Analytics access, while `youtubeRetentionAPI` remains the source for
platform metric definitions. The rebuilt PDF contains 45 reference entries;
the former repeated-author OAuth entry is absent. The deterministic reference
audit reports PASS with 45 cited keys, 45 BibTeX entries, no unused keys, no
missing keys, and complete evidence-matrix coverage. The reference pages were
visually checked after the rebuild; no interleaved figure or clipping was found.

## Reference-density expansion QA (historical, 2026-09-16)

After the bibliography grew from 17 to 46 verified entries, the changed pages
were re-rendered with MiKTeX Poppler `pdftoppm` at 120 dpi into
`tmp/pdf_qa/reference_expansion_20260916/` (pages 1, 2, 4, 7, 13, 14, 15).
The corrected bibliography was additionally rendered into
`tmp/pdf_qa/reference_update_20260916_v2/`; its contact sheet and representative
pages were inspected directly, supplemented by geometry and text-layer checks:

- the historical 46-entry build rendered all 46 reference numbers in
  first-appearance order on pages 14--15,
  with none missing and no unresolved `??` markers anywhere in the document;
- proper nouns rendered correctly in that historical reference list (including
  the then-present OAuth entry, which was removed in the cleanup above,
  alongside "OpenAI Codex", "AI-assisted coding", "FreeSurfer", "V-JEPA 2",
  "LightGBM", and "TikTok");
- DOI resolver links render for DOI-bearing entries; the RAND report uses its
  official RAND URL because the previously listed `.1` DOI suffix could not be
  verified;
- word-bounding-box checks found no text outside the page margins and no
  body-text crossings of the two-column gutter; the only center-spanning
  words belong to intentional full-width elements (title-page abstract and
  full-width `figure*`/`table*` captions and tables);
- BibTeX completed with zero warnings; both package test suites pass.

Details of source verification are in `reference_search_log.md` and
claim-level mapping in `reference_evidence_matrix.md`. A final author review
is still required for submission-specific metadata and declarations.

## Non-blocking compiler diagnostics

The IEEE Access class emits repeated `Overfull \\hbox (505.12177pt)` messages
from its template output routine and font fallback warnings for the supplied
Formata font. The rendered pages were inspected and show no corresponding
visible defect. These diagnostics should be rechecked if the template or
author metadata changes.

## Completed audit gates

- Position-adjusted associations were checked with the prespecified cubic
  position adjustment and a 500 circular-shift null audit.
- The nonlinear Appendix audit uses a same-family grouped/chronological
  HistGradientBoosting comparator rather than an incomparable model family.
- The matched pattern-change control analysis was generated from the frozen
  retention/TRIBE release.
- `python -m pytest -q tests/test_ieee_access_submission_audit.py`: 5 passed.
- `python -m pytest -q tests/test_audit_ieee_access_references.py`: 5 passed.
- `python scripts/audit_ieee_access_references.py --root paper/IEEE_access
  --write-report`: pass.

Audit outputs are under `data/submission_audit/` and are referenced by the
manuscript Appendix and audit manifest.

## Submission blockers

This remains an author-review draft. Before submission, replace author,
affiliation, correspondence, ORCID, funding, ethics determination, data and
code access route, DOI/history placeholders, and every biography placeholder.
The audit gates are complete; they should be rechecked only if source data,
figures, or the analysis code changes.
