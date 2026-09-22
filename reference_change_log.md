# IEEE Access Reference Change Log

Date: 2026-09-16

## Bibliography changes (reference-density expansion, 2026-09-16 later pass)

- Before: 17 cited entries.
- After: 46 cited entries (29 additions, 0 removals).
- Added, brain-encoding and naturalistic neuroimaging lineage:
  `dascoli2025tribe`, `villanueva2025predicting`, `kay2008identifying`,
  `naselaris2011encoding`, `yamins2014performance`, `wen2018neural`,
  and `fischl2012freesurfer` (resolves the previously uncited fsaverage5
  surface geometry).
- Added, multimodal video/audio/language representation and TRIBE v2
  backbone provenance: `assran2025vjepa2`, `chung2021w2vbert`,
  `grattafiori2024llama3`, `radford2021clip`, `feichtenhofer2019slowfast`,
  and `baltrusaitis2019multimodal`.
- Added, audience-behavior, short-form format, and institutional
  communication: `kim2014dropouts`, `breslow2013studying`,
  `rajendran2024shorts`, `kaye2022tiktok`, `rice2013campaigns`, and
  `dertouzos2003military`.
- Added, statistical and methodological grounding: `shmueli2010explain`,
  `theiler1992surrogate`, `hastie2009esl`, `bertrand2004did`,
  `ke2017lightgbm`, `recht2019imagenet`, `nosek2018preregistration`,
  `wilkinson2016fair`, `nardo2005composite`, and `shadish2002experimental`.
- Formatting: brace-protected proper nouns in the three `@misc` entries
  (YouTube, OAuth, OpenAI, AI now render with correct capitalization),
  removed the redundant `howpublished = {Online}` duplication, and added
  `url` fields carrying the DOI resolver link so DOIs render in the
  reference list despite stock `IEEEtran.bst` ignoring the `doi` field.
- Every added record was verified against arXiv, Crossref, ACM, PMLR,
  NeurIPS proceedings, RAND, or JRC repository pages before inclusion;
  the verification trail is in `reference_search_log.md`. A candidate
  brain-encoding reference ("BrainSLM") was rejected because no
  authoritative record could be located.
- Three candidate records initially recalled from memory were corrected
  during verification: Yamins et al. 2014 is PNAS (not Nature
  Neuroscience), the SlowFast ICCV DOI is 10.1109/ICCV.2019.00630, and
  the Wav2Vec-BERT 2.0 citation is the Chung et al. W2v-BERT record rather
  than the unrelated MMS/wav2vec 2.0 arXiv record. The RAND military-media
  record retains its official RAND URL and no longer carries the
  unverified `.1` DOI suffix.

## Prose changes (reference-density expansion)

- Introduction: grounded the short-form-format and institutional
  communication framing sentence, which previously had no citation.
- Related Work: all four subsections expanded with the verified lineage
  above; positioning sentences keep the rule that cited lineages motivate
  but do not validate the present channel application.
- Method 4.1: added backbone provenance sentences (frozen V-JEPA 2,
  W2v-BERT 2.0, Llama 3.2 feature extraction) and the FreeSurfer
  citation for fsaverage5; no result numbers were touched.
- Method 4.3: grounded the position-effect claim (in-video dropout
  studies, multimedia segmenting), the cubic trend removal, and the
  surrogate-data spirit of the circular-shift null.
- Method 4.4 and Appendix B: grounded the HistGradientBoosting design
  lineage and the differences-in-differences contrast construction.
- Method 4.6: grounded artifact stewardship wording on the FAIR
  principles.
- Discussion: grounded four general methodological statements (composite
  aggregation, distribution shift, preregistration, experimental design).
  Own-result interpretation sentences remain intentionally uncited.
- Results, Conclusion, abstract, author placeholders, ethics and
  data-availability draft statements: unchanged.

## Earlier bibliography changes (2026-09-16 first pass)

- Before: 12 BibTeX entries, including one unused FDR entry and one unused
  general YouTube API entry after prose narrowing.
- After: 16 cited entries.
- Added: `nishimoto2011naturalmovies`, `huth2016naturalspeech`,
  `efron1979bootstrap`, `hoerl1970ridge`, `varma2006crossvalidation`,
  `jolliffe2016pca`, `pedregosa2011scikit`, and `youtubeAuthScopes`.
- Removed: `benjamini1995fdr` because no FDR procedure remains in the paper;
  `youtubeAnalyticsAPI` because the more specific retention and authorization
  sources cover every remaining YouTube claim.
- Updated: YouTube and Codex access dates to September 16, 2026; the TRIBE
  record remains explicitly identified as an arXiv preprint.

## Earlier prose changes

- Replaced the abstract's broad opening platform claim with a study-specific
  statement so the abstract remains citation-free.
- Narrowed the introduction's short-form-video statement to the settings
  directly supported by the educational-video and multimedia-learning sources.
- Added official definitions for retention metrics and authorization scopes.
- Added naturalistic visual/speech neuroimaging context without presenting it
  as validation of the present channel application.
- Added direct method citations for Spearman association, bootstrap intervals,
  Ridge regression, PCA, cross-validation model-selection bias, and
  scikit-learn software provenance.
- Replaced the unsupported list of possible cross-channel confounders with a
  statement limited to the observed design difference between channels.
- Added the Destrieux source at first use of the atlas-based parcel masks.

## Validation record

- `reference_evidence_matrix.md` maps every external claim block to a direct
  source and identifies own-result blocks that should not receive an external
  citation. All 46 keys are covered.
- `reference_search_log.md` records source URLs, evidence concepts, decisions,
  and exclusions.
- `scripts/audit_ieee_access_references.py` performs deterministic citation and
  BibTeX integrity checks without network access.
- `python -m pytest -q tests/test_audit_ieee_access_references.py` and
  `python -m pytest -q tests/test_ieee_access_submission_audit.py`: both pass
  after the expansion (5 tests each).
- LaTeX compilation and rendered-PDF visual QA are rerun after this change;
  final page count and artifact size are recorded in `PDF_QA.md`.

## Bibliography integrity cleanup (2026-09-22)

- Removed `youtubeAuthScopes` from the manuscript and bibliography. The paper
  retains the study fact that the channel owner authorized read-only Analytics
  access, but the OAuth implementation details are not part of the scientific
  contribution or an interpretation claim.
- Retained `youtubeRetentionAPI` as the sole external source for the platform's
  audience-watch-ratio and relative-retention definitions.
- Re-audited the remaining 45 bibliography records against the source ledger;
  no fabricated record was identified. arXiv records remain explicitly treated
  as preprints.
