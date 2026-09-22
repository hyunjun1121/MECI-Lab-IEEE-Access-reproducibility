# IEEE Access submission requirements and package status

Checked on 2026-09-15 against the official IEEE Access author pages and the supplied IEEE Access LaTeX template.

## Requirements confirmed from IEEE Access

| Requirement | Package implementation or status |
|---|---|
| Manuscript type | Use `Research Article`. IEEE Access describes this as the standard article type for an investigation with a result of value to the field. |
| File format | Submit the official double-column, single-spaced IEEE Access template source and a matching PDF. The official submission page states that each file must be no larger than 40 MB. |
| Page length | IEEE Access has no fixed page limit for regular articles and no over-length page charge, but strongly recommends fewer than 20 pages for readability. A regular article that needs to exceed 20 pages for a special reason should make a pre-submission inquiry to the Editor-in-Chief. The recommendation explicitly excludes Supplementary Material and Appendices from that 20-page count; this is not an unlimited-content allowance. Supplementary files remain part of the review package and should be limited to material that is necessary, readable, legally shareable, and technically supported. |
| Abstract | The supplied template requires one self-contained, unstructured paragraph of 150--250 words without citations, footnotes, displayed equations, or tables. |
| Index Terms | Provide 3--10 accurate terms. The draft uses seven terms and will be checked against the IEEE Thesaurus before submission. |
| Acronyms | Define every abbreviation at first use in the abstract and again at first use in the body when necessary. |
| Figures and tables | Use the template, cite figures and tables in numerical order, place figure captions below figures and table captions above tables, and submit editable source material where required by the portal. |
| References | Use numbered IEEE citations in order of first appearance and verify every reference for accuracy and relevance. |
| Author metadata | List every author in the source and PDF. The corresponding author needs a visible, populated ORCID in the submission system. |
| Author biographies | Include a short biography for every author below the reference list, as supported by the template. Author photographs are optional only if the appropriate no-photo biography environment is used. |
| AI-generated text | Disclose use of artificial intelligence in the Acknowledgment section. IEEE's submission page also requires citations to the AI system for sections that use AI-generated text. The draft contains a clearly marked disclosure that requires author approval and final journal-policy review. |
| Supplementary material | IEEE Access allows supplementary material such as code and data to be submitted for review and, if published, displayed with the article. Use it for extended tables, additional figures, code documentation, data dictionaries, and robustness details after the main argument is understandable without it. There is no stated blanket unlimited size or page allowance: the portal, file-size limits, readability, copyright, privacy, and reviewability still govern what should be uploaded. |
| Reproducibility | Provide enough method detail and, where possible, code, data, documentation, environment information, and persistent versioning. Private Analytics data and raw video are not redistributed; the access route must be stated precisely. |
| Multimedia | If submitted, video files are subject to the official maximum size stated on the author page. No video is included in this draft package. |

## Official sources

- Submission Guidelines: <https://ieeeaccess.ieee.org/authors/submission-guidelines/>
- About IEEE Access and scope: <https://ieeeaccess.ieee.org/about/>
- Reproducibility: <https://ieeeaccess.ieee.org/authors/reproducibility/>
- Reviewer Guidelines: <https://ieeeaccess.ieee.org/reviewers/reviewer-guidelines/>
- IEEE Access LaTeX template selector: <https://template-selector.ieee.org/>
- IEEE Thesaurus: <https://www.ieee.org/content/ieee-org/en/publications/services/thesaurus.html>

## Draft acceptance gate

The package is not submission-ready until all of the following are resolved:

1. Author names, order, affiliations, correspondence, ORCID, biographies, and funding are approved.
2. Ethics or institutional determination for public-video and owner-authorized aggregate Analytics data is approved and stated.
3. The data-availability and code-availability route is approved, including any restrictions imposed by YouTube Analytics, TRIBE v2, Hugging Face, or institutional policy.
4. The completed circular-shift null control is reviewed against `data/submission_audit/audit_manifest.json` and the selected table values.
5. The completed same-family boosted-model comparator is reviewed if its Appendix results remain in the manuscript; it is not used to replace the primary interpretable Ridge comparison.
6. The final manuscript is checked for source/PDF identity, page count, figure order, reference order, abstract length, Index Terms, author biographies, and AI disclosure.
7. The final PDF is visually inspected after compilation, and the source and PDF remain under the portal file-size limit.

## Scope boundary

The manuscript does not claim that TRIBE v2 predicts actual viewer brain activity, learning, psychological state, or military readiness. It evaluates a content-analysis procedure using model-derived representations and owner-authorized platform aggregates. All exploratory screens, KFN transfer results, and any post hoc choices must remain labeled as exploratory or auxiliary.
