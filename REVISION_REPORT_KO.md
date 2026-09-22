# IEEE Access 수정 보고서

기준 문서: `IEEE_Access_논문수정_에이전트프롬프트.md`와 주석 PDF
`IEEE_Access_브레인모델링_의견 포함 260919.pdf`.

## 처리 원칙

원래 추론 코드, 실행 설정, 저장된 분석 CSV를 우선 근거로 삼았다. 확인된
수치만 원고에 반영했고, 사전등록·인과효과·개인 시청자 심리와 같이 자료가
보장하지 않는 주장은 추가하지 않았다. 새로 계산한 결과는 없으며, Figure
5--7은 기존의 공개 가능한 집계 CSV를 같은 분석 계열 안에서 다시 그렸다.

## 항목별 처리 결과

| ID | 상태 | 처리 내용 | 근거 및 위치 |
|---|---|---|---|
| C01 | 반영 | 197편에서 194편으로 줄어든 이유를 unmatched-word ratio `> 0.05`로 정의하고, 세 영상의 실제 `1/18`, `1/1`, `1/7` 기록과 예측 전 제외, 비폴백 실행을 명시했다. 설정에 고정되어 있었지만 사전등록은 아니라고 구분했다. | `main.tex` Data and Study Design, `data/video_status.json`, 서버 진단 JSON |
| C02 | 반영 | 190편 retention, 140편 region-profile association, 109편 temporal-change association을 서로 다른 적격 조건으로 분리했다. 140/109는 영상 단위 요약이며, 최소 8개 유효 5초 관측과 변화량의 추가 결측·상수값 조건을 표에 명시했다. | `main.tex` Table 1 및 Method, `data/continuous_association_summary.csv` |
| C03 | 반영 | 4초·64프레임 모델 입력, 1초 persisted cortical interval, 5초 overlap-weighted analysis window를 분리했다. 불완전 coverage와 결측 Analytics bin은 창에서 제외하고 추가 지연은 넣지 않았음을 명시했다. | `main.tex` Method, `appendix.tex`, `data/feature_dictionary.csv`, `surface_summaries/*.npz` 전수 검증 |
| C04 | 반영 | `exit_intensity = stoppedWatching / totalSegmentImpressions`로 정의하고 API 1% bin을 시간 중첩에 따라 분할·합산했다. 결측 bin, 0 또는 비유한 분모는 결측으로 두며 개인 이탈확률·hazard가 아니라고 명시했다. | `main.tex` Method, `scripts/yugsa_retention_common.py` |
| C05 | 반영 | 기존 단순 event 전후 결과와 혼동하지 않도록 Figure 6을 세 outcome별 Event/Control/Event-Control 패널로 교체했다. 92쌍·84편, 5초 창, 95% video-bootstrap interval, 평균 위치거리 0.1918을 본문과 부록에 반영했다. 인과적 DiD가 아닌 기술적 pre-post contrast로 명시했다. | `main.tex`, `appendix.tex`, `figures/05_pattern_change_events.pdf`, `data/submission_audit/matched_pattern_change_control_summary.csv` |
| C06 | 반영 | 게시 전에는 모델-derived descriptor로 검토 후보를 지명할 수 있고, 게시 후에는 관측된 platform outcome과 정렬해 공동 검토할 수 있다는 두 단계로 Discussion을 재작성했다. 편집 개선 효과나 교육효과가 입증되었다고 쓰지 않았다. | `main.tex` Discussion |
| C07 | 반영 | 여섯 profile을 viewer psychological state가 아닌 model-derived content feature로 정의하고, 명칭이 실제 reward·aversion·social valuation·engagement 발생을 뜻하지 않는다고 통합 서술했다. exit-intensity에서의 outcome-specific 추가 정보와 일반 예측 가능성을 구분했다. | `main.tex` Method/Results/Discussion, `appendix.tex` Table 2 |
| C08 | 반영 | 핵심 Figure 6에서 secondary `Start intensity`를 제외했다. 주 분석은 audience watch ratio, relative retention performance, exit intensity 세 outcome으로 유지하고, secondary 결과를 설명 없이 삭제하지 않았다. | `main.tex`, `appendix.tex`, 원래 분석 설정 및 보조 산출물 |
| C09 | 반영 | Conclusion을 시간 국소적 editorial review 후보와 고정된 평가 설계에서의 outcome-specific 추가 정보라는 실제 기여로 조정했다. 모든 outcome·채널·교육효과로 일반화하지 않았다. | `main.tex` Conclusion 및 Abstract/Discussion 정합성 확인 |
| C10 | 반영 | Table 7 열 제목을 `High-watch minus low-watch profile mean`으로 바꾸고, within-video top/bottom quartile profile mean 차이임을 설명했다. 음수는 high-watch 창의 model-derived profile 값이 낮았다는 기술적 의미일 뿐 인과효과나 viewer state가 아님을 명시했다. | `appendix.tex` Table 7 설명 및 표 |
| A01 | 반영 | Figure 7을 association 그림이 아니라 `cross_channel_transfer.csv`의 held-out R² 그림으로 교체했다. 방향별 Metadata/Metadata+ROI, zero line, 194/2,312 표본 수를 표시하고 음의 R²를 음의 상관이 아닌 test-set mean baseline 미달로 설명했다. | `build_review_figures.py`, `figures/03_cross_channel.pdf`, `main.tex` Results |
| A02 | 반영 | Figure 5를 동일 Ridge 계열의 Metadata, Metadata+ROI, Metadata+ROI+changes 비교로 교체했다. grouped/chronological split, video-equal MAE, `MAE_metadata - MAE_enriched` 부호를 명시했다. HistGradientBoosting 비교는 Appendix에만 남겼다. | `build_review_figures.py`, `main.tex` Table 5/Results, `data/submission_audit/fair_model_metrics.csv` |
| A03 | 반영 | `pattern_change`를 `1 - correlation`으로 통일하고, 각 whole-cortex vector의 평균 제거·인접 5초 overlap-weighted vector·첫 비교/상수 벡터 결측 처리를 명시했다. `correlation distance`라는 부정확한 데이터 사전 표현을 수정했다. | `main.tex`, `appendix.tex`, `data/feature_dictionary.csv`, `scripts/yugsa_extended_analysis.py` |
| A04 | 반영 | grouped Ridge 개선량 `0.000283` [0.000124, 0.000442]와 chronological `0.000386` [-0.000013, 0.000791]을 구분했다. 후자의 구간이 0을 포함하므로 두 평가에서 동일하게 확정적이라고 쓰지 않았다. | `main.tex` Results, `data/submission_audit/fair_model_paired_improvement.csv` |

## 수치 변경 기록

주요 결과 수치의 원자료 값은 변경하지 않았다. 변경된 것은 잘못 대응된
Figure 5--7의 시각화와, 본문·표·캡션의 분석 정의 및 표본 설명이다. Figure
6은 기존 `pattern_change_event_summary.csv`의 93개 event 전후 차트를 본문 주
분석으로 사용하지 않고, 원고에서 채택한
`matched_pattern_change_control_summary.csv`의 92쌍/84편 결과와 일치하도록
재생성했다. 이는 값의 유리한 선택이 아니라 그림·본문 분석 대상 불일치
수정이다.

## 검증

- 원래 코드에서 4초 입력, 1초 저장 interval, 5초 primary window,
  중첩가중 집계를 확인했다.
- 194개 strict output의 persisted interval duration을 전수 검사했다.
- 190/140/109/84/92/1,745 수치를 CSV·JSON·원고 간 대조했다.
- Figure 5--7을 벡터 PDF로 재생성하고 `main.pdf` 재컴파일 후 변경 페이지를
  이미지로 확인한다.
- 저자·소속·윤리·연구비·데이터 공개 경로·ORCID placeholder는 창작하지
  않고 별도 미해결 목록에 남겼다.
