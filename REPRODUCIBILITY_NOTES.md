# 재현성 메모

이 문서는 현재 패키지의 문서 컴파일과 Figure 5--7 재생성 범위를 설명한다.
전체 TRIBE v2 추론·YouTube 수집·OAuth 재인증은 이 패키지에서 수행하지 않는다.

## 원고 컴파일

PowerShell에서:

```powershell
cd C:\project\MECI-Lab\paper\IEEE_access
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

최종 산출물은 `main.pdf`이며, `main.bbl`은 `references.bib`에서 생성된
빌드 산출물이다. 그림과 참고문헌 변경 후에는 네 단계를 다시 실행한다.

## Figure 5--7 재생성

저장소 루트에서 실행한다:

```powershell
cd C:\project\MECI-Lab
python paper\IEEE_access\build_review_figures.py
```

이 스크립트는 다음 입력만 읽고 세 개의 벡터 PDF와 provenance JSON을 만든다.

| 출력 | 입력 | 의미 |
|---|---|---|
| `figures/02_predictive_increment.pdf` | `data/submission_audit/fair_model_metrics.csv` | 동일 Ridge 계열의 Metadata/ROI/ROI+changes video-equal MAE 비교 |
| `figures/05_pattern_change_events.pdf` | `data/submission_audit/matched_pattern_change_control_summary.csv` | 92 matched pairs/84 videos의 event, control, event-control 변화 |
| `figures/03_cross_channel.pdf` | `data/cross_channel_transfer.csv` | YugsaTV↔KFN held-out transfer R²와 zero baseline |
| `data/review_figure_provenance.json` | 위 세 입력 및 출력 | 입력·출력 상대경로와 SHA-256 |

Figure 1 생성기 `build_pipeline_figure.py`는 별도 비공개 source media와
private analysis response에 의존하며, 이 패키지의 일반 재현 범위에 포함하지
않는다. Figure 2--4와 Appendix Figure 8은 패키지에 포함된 기존 PDF를 사용한다.

## 분석 정의의 핵심

- 모델 입력: 4초, 64-frame clip
- persisted cortical output: 1초 interval
- primary analysis window: 5초, temporal-overlap weighting
- primary model evaluation: video-grouped Ridge; chronological 80/20은 보조 확인
- MAE: video-equal mean absolute error
- pattern change: adjacent within-vector-centered whole-cortex vectors의
  `1 - correlation`; 첫 비교와 constant vector는 결측
- event display: top-decile pattern-change 후보, 최소 10초 간격, 같은 영상의
  nearest non-event control, 92쌍/84편 완전 사례

상세 계산 규칙은 `main.tex`, `appendix.tex`,
`data/feature_dictionary.csv`, `data/submission_audit/audit_manifest.json`,
그리고 저장소의 `scripts/yugsa_extended_analysis.py`에 있다.

## 재현 범위의 한계

패키지는 raw media, raw owner Analytics JSON, OAuth credentials, model weights,
runtime caches를 제외한다. 따라서 이 ZIP만으로 처음부터 TRIBE 추론이나
Analytics API 재수집을 수행할 수는 없다. 대신 공개 가능한 집계 표·감사
자료와 Figure 5--7은 재생성할 수 있고, `main.pdf`는 바로 검토할 수 있다.
