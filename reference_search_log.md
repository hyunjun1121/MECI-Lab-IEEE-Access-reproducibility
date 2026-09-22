# IEEE Access Reference Search Log

Search and verification date: 2026-09-16

## Source hierarchy

Primary model papers, original methods papers, official platform
documentation, and the official software publication were preferred. Search
results were used only to locate the authoritative record; the manuscript
does not cite search-result pages. A source was added only when its record
matched the nearby claim and bibliographic metadata could be checked.

## Search record (reference-density expansion, 2026-09-16 later pass)

All records below were verified through arXiv abstract pages, the Crossref
API (`api.crossref.org/works/<DOI>`), ACM DL, PMLR proceedings pages,
NeurIPS proceedings pages, the RAND record, or the JRC publications
repository before inclusion.

| Topic | Authoritative record | Evidence used | Decision |
|---|---|---|---|
| TRIBE v1 lineage | [arXiv:2507.22229](https://arxiv.org/abs/2507.22229) | Title, five-author list, tri-modal encoder purpose | Add `dascoli2025tribe` as lineage; no peer-review claim. |
| Parallel multimodal movie-response work | [arXiv:2507.19956](https://arxiv.org/abs/2507.19956) | Title, six-author MedARC list, pretrained multimodal features for movie fMRI | Add `villanueva2025predicting` as parallel work only. |
| Natural-image identification | [Crossref 10.1038/nature06713](https://api.crossref.org/works/10.1038/nature06713) | Nature 452(7185):352–355 metadata | Add `kay2008identifying`. |
| Encoding/decoding framework | [Crossref 10.1016/j.neuroimage.2010.07.073](https://api.crossref.org/works/10.1016/j.neuroimage.2010.07.073) | NeuroImage 56(2):400–410 metadata | Add `naselaris2011encoding`. |
| DNN-cortex correspondence | [PNAS DOI record](https://doi.org/10.1073/pnas.1403112111) | PNAS 111(23):8619–8624; corrected venue (PNAS, not Nature Neuroscience as first recalled) | Add `yamins2014performance`. |
| Dynamic natural-vision encoding | [Crossref 10.1093/cercor/bhx268](https://api.crossref.org/works/10.1093/cercor/bhx268) | Cerebral Cortex 28(12):4136–4160 metadata | Add `wen2018neural`. |
| FreeSurfer / fsaverage5 | [Crossref 10.1016/j.neuroimage.2012.01.021](https://api.crossref.org/works/10.1016/j.neuroimage.2012.01.021) | NeuroImage 62(2):774–781 metadata | Add `fischl2012freesurfer`; resolves the uncited fsaverage5 geometry. |
| V-JEPA 2 visual backbone | [arXiv:2506.09985](https://arxiv.org/abs/2506.09985) | Title, first six authors, self-supervised video model purpose; also confirmed as TRIBE v2's visual stream in the TRIBE v2 full text | Add `assran2025vjepa2`. |
| TRIBE v2 backbone configuration | [arXiv:2605.04326 full text](https://arxiv.org/html/2605.04326v1) | Section 5.2 names frozen Video-JEPA-2, Wav2Vec-Bert-2.0, and Llama-3.2-3B extractors | Supports the Method 4.1 backbone sentences; no separate citation. |
| Wav2Vec-BERT 2.0 audio backbone | [IEEE ASRU record](https://ieeexplore.ieee.org/document/9688253/) / [arXiv:2108.06209](https://arxiv.org/abs/2108.06209) | Chung et al. record the W2v-BERT self-supervised speech pre-training method; the TRIBE v2 full text identifies Wav2Vec-Bert-2.0 as the persisted auditory extractor | Add `chung2021w2vbert`; do not use the unrelated MMS/wav2vec 2.0 paper as the backbone source. |
| Llama 3 text backbone | [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) | Title, first authors, 2024 submission | Add `grattafiori2024llama3`. |
| Image–language contrastive model | [PMLR v139 record](https://proceedings.mlr.press/v139/radford21a.html) | CLIP title, authors, PMLR 139:8748–8763 | Add `radford2021clip`. |
| Multi-rate video architecture | [IEEE DOI record](https://doi.org/10.1109/ICCV.2019.00630) | ICCV 2019 pages 6201–6210; corrected DOI (an initially recalled DOI resolved to an unrelated ICCV paper) | Add `feichtenhofer2019slowfast`. |
| Multimodal survey | [Crossref 10.1109/TPAMI.2018.2798607](https://api.crossref.org/works/10.1109/TPAMI.2018.2798607) | IEEE TPAMI 41(2):423–443 metadata | Add `baltrusaitis2019multimodal`. |
| In-video dropouts | [ACM DOI record](https://doi.org/10.1145/2556325.2566237) | L@S '14 pp. 31–40, six-author list, position-dependent dropout evidence | Add `kim2014dropouts`; direct support for the position-effect sentences. |
| edX first-MOOC report | [RPA journal record](https://www.rpajournal.com/studying-learning-in-the-worldwide-classroom-research-into-edxs-first-mooc/) | Research & Practice in Assessment 8(1):13–25 | Add `breslow2013studying`. |
| YouTube Shorts empirical study | [arXiv:2402.18208](https://arxiv.org/abs/2402.18208) | Title, three authors, Shorts/long-form engagement analysis | Add `rajendran2024shorts` as an arXiv record; no causal wording. |
| Short-video culture monograph | [Polity book record](https://philpapers.org/rec/KAYTCA-4) | Polity Press 2022 monograph metadata, scholarly citations | Add `kaye2022tiktok`. |
| Public communication campaigns | [Annual Reviews citing record](https://www.annualreviews.org/content/journals/10.1146/annurev-publhealth-071723-120721) | Cross-checked 4th-edition metadata (Rice & Atkin, Eds., SAGE, 2012/2013) against several independent citing records (Annual Reviews, PMC, SAGE journals) | Add `rice2013campaigns` for institutional-communication background. |
| Military media evaluation | [RAND MR-1591 record](https://www.rand.org/pubs/monograph_reports/MR1591.html) / [JSTOR stable record](https://www.jstor.org/stable/10.7249/mr1591osd) | RAND monograph metadata, MR-1591-OSD, 2003; the stable record is used as a link, with no unverified DOI field retained | Add `dertouzos2003military` as context on institutional media evaluation; no effectiveness claim transferred. |
| Explain vs predict | [Crossref 10.1214/10-STS330](https://api.crossref.org/works/10.1214/10-STS330) | Statistical Science 25(3) metadata | Add `shmueli2010explain`. |
| Distribution shift | [PMLR v97 record](https://proceedings.mlr.press/v97/recht19a.html) | ICML 2019, PMLR 97:5389–5400 | Add `recht2019imagenet`. |
| Preregistration | [Crossref 10.1073/pnas.1708274114](https://api.crossref.org/works/10.1073/pnas.1708274114) | PNAS 115(11):2600–2606 metadata | Add `nosek2018preregistration`. |
| FAIR principles | [Crossref 10.1038/sdata.2016.18](https://api.crossref.org/works/10.1038/sdata.2016.18) | Scientific Data 3:160018 metadata | Add `wilkinson2016fair`. |
| Surrogate data | [Crossref 10.1016/0167-2789(92)90102-S](https://doi.org/10.1016/0167-2789(92)90102-S) | Physica D 58(1–4):77–94 metadata | Add `theiler1992surrogate`; own shift parameters remain internal. |
| Differences-in-differences | [Crossref 10.1162/003355304772839588](https://api.crossref.org/works/10.1162/003355304772839588) | QJE 119(1):249–275 metadata | Add `bertrand2004did`. |
| LightGBM | [NeurIPS proceedings record](https://proceedings.neurips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf) | NIPS 30 pp. 3149–3157, eight-author list | Add `ke2017lightgbm` as HistGradientBoosting design lineage. |
| Elements of Statistical Learning | [Crossref 10.1007/978-0-387-84858-7](https://api.crossref.org/works/10.1007/978-0-387-84858-7) | Springer 2nd-edition book metadata | Add `hastie2009esl` for spline/polynomial trend-removal practice. |
| Composite indicators | [JRC repository record](https://publications.jrc.ec.europa.eu/repository/handle/JRC31473) | EUR 21682 EN report metadata | Add `nardo2005composite`. |
| Experimental design reference | Standard bibliographic record (Shadish, Cook, and Campbell, Houghton Mifflin, 2002) | Canonical experimental-design book | Add `shadish2002experimental`. |

Exclusions during this pass:

- A candidate "BrainSLM" brain-encoding reference was rejected: repeated
  searches returned no authoritative record, so no entry was created.
- Addiction- and attention-span-framed short-form studies from low-verifiability
  venues were not used; the arXiv Shorts study and the Polity monograph cover
  the format claims with wording the sources directly support.

## Earlier search record (2026-09-16 first pass)

| Topic | Authoritative record | Evidence used | Decision |
|---|---|---|---|
| TRIBE v2 model | [arXiv:2605.04326](https://arxiv.org/abs/2605.04326) | Title, authors, tri-modal vision/audition/language framing, and cortical prediction purpose | Retain as an arXiv/preprint record. The manuscript does not call it peer-reviewed or published. |
| YouTube retention reports | [Channel reports](https://developers.google.com/youtube/analytics/channel_reports) | Retention dimensions and elapsed-video-position reporting | Retain as the platform definition source through `youtubeRetentionAPI`. |
| YouTube metric definitions | [Analytics metrics](https://developers.google.com/youtube/analytics/metrics) | Audience watch ratio, repeat watching, and relative retention definitions | Retain through `youtubeRetentionAPI`. |
| YouTube report queries | [Reports and dimensions](https://developers.google.com/youtube/analytics/reference) | Report-query structure and available dimensions/metrics | Retain through `youtubeRetentionAPI`. |
| Cortical parcellation | [PubMed record](https://pubmed.ncbi.nlm.nih.gov/20547229/) | Destrieux atlas paper title, journal, volume, pages, and DOI | Retain `destrieux2010parcellation`; use for spatial boundaries, not psychological labels. |
| Educational video production | [ACM DOI record](https://doi.org/10.1145/2556325.2566239) | Guo, Kim, and Rubin empirical MOOC-video engagement study | Retain `guo2014video`; limit wording to the observed educational-video setting. |
| Multimedia learning | [Cambridge DOI record](https://doi.org/10.1017/CBO9780511811678) | Mayer book record and multimedia-learning framework | Retain `mayer2009multimedia` for the conceptual background claim. |
| Learning analytics interpretation | [TechTrends DOI record](https://doi.org/10.1007/s11528-014-0822-x) | Behavioral traces require a substantive learning question | Retain `gasevic2015learning` for the interpretation boundary. |
| Prediction versus explanation | [SAGE DOI record](https://doi.org/10.1177/1745691617693393) | Different goals and designs for prediction and explanation | Retain `yarkoni2017prediction`. |
| Natural movie representations | [Current Biology DOI record](https://doi.org/10.1016/j.cub.2011.08.031) | Distributed cortical representation of natural movie-evoked activity | Add `nishimoto2011naturalmovies` with visual-only wording. |
| Natural speech representations | [Nature DOI record](https://doi.org/10.1038/nature17637) | Distributed semantic maps for natural speech | Add `huth2016naturalspeech` with speech-specific wording. |
| Spearman association | [JSTOR DOI record](https://doi.org/10.2307/1412159) | Original rank-association method record | Retain `spearman1904association`. |
| Ridge regression | [Technometrics DOI record](https://doi.org/10.1080/00401706.1970.10488634) | Original Ridge regression method record | Add `hoerl1970ridge`. |
| Bootstrap | [Annals of Statistics DOI record](https://doi.org/10.1214/AOS/1176344552) | Original bootstrap method record | Add `efron1979bootstrap`; own repetition count remains internal. |
| PCA | [Philosophical Transactions DOI record](https://doi.org/10.1098/rsta.2015.0202) | PCA review and dimensionality-reduction context | Add `jolliffe2016pca`; own explained-variance value remains internal. |
| Cross-validation bias | [BMC Bioinformatics DOI record](https://doi.org/10.1186/1471-2105-7-91) | Model-selection leakage can bias error estimation | Add `varma2006crossvalidation`. |
| scikit-learn | [JMLR software paper](https://www.jmlr.org/papers/v12/pedregosa11a.html) | Software provenance for the fixed implementation family | Add `pedregosa2011scikit`; no estimator-specific attribution is made. |
| AI-use acknowledgment | [OpenAI Codex](https://openai.com/codex/) | Tool identity for the draft acknowledgment only | Retain `openAICodex`; it is not scientific evidence. |

## Exclusions and checks

- The former `benjamini1995fdr` entry was removed because the current paper
  explicitly treats the circular-shift audit as a design diagnostic and does
  not report an FDR-controlled significance procedure.
- No source was added for the manuscript's own counts, metrics, figures,
  frozen snapshots, or transfer results; those are supported by internal
  manifests and tables.
- No secondary blog, vendor summary, or search-result page was used as a
  citation.
- No source was used to imply that a TRIBE prediction is measured viewer
  neurophysiology, a psychological state, learning, or a causal mechanism.
- The deterministic audit script checks key coverage, unused entries, DOI
  uniqueness, required metadata, placeholders, and evidence-matrix coverage.
