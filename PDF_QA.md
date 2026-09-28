# Public Release QA

Checked: 2026-09-28

- `main.pdf`: 14 pages; 2,111,221 bytes; SHA-256
  `1b0a04af5db99c912d6077b93271c31a22701fc172178e54aaf510250e9c31f2`.
- The final PDF was compiled from the adjacent LaTeX source. The appendix and
  reference end pages were re-rendered and checked after the public-scope
  clarification; no clipping or text collision was observed.
- The bibliography audit passes with 45 cited keys and 45 BibTeX entries, no
  unused or missing keys, no duplicate DOI, and complete evidence-matrix
  coverage.
- The public Zenodo record is open, version 1.0.0, and contains the single
  code-and-aggregate-results archive under DOI
  `10.5281/zenodo.22916779`.
- The archive recreates selected figures from released aggregates; it does not
  rerun TRIBE v2 inference or recollect YouTube Analytics data.
- Video- and window-level Analytics-derived records, internal work notes,
  credentials, raw media, model weights, and runtime caches are absent from the
  cleaned public repository tree and Zenodo archive. The appendix explicitly
  distinguishes internal audit manifests from the released aggregate files.

This record describes package checks. It is not an IEEE editorial decision or
a substitute for final author approval of the manuscript and declarations.
