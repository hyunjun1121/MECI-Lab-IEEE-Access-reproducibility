# 미해결 사항 및 저자 확인 요청

현재 수정은 분석 코드와 집계 산출물로 확인 가능한 범위까지 완료했다.
아래 항목은 사실을 추정해 채우지 않았으며, 제출 전에 저자가 결정해야 한다.

## 저자·제출 메타데이터

- 네 저자의 짧은 biography 원고
- 네 저자의 ORCID 연결 및 제출 시스템 metadata
- 연구비, 이해상충, 감사의 글에 대한 최종 저자 확인
- 기관의 윤리 검토·면제·비해당 판단 문구에 대한 최종 확인
- AI 사용 공개 문구와 저자 책임에 대한 최종 확인

## 데이터 공개 경로

원고에는 공개 GitHub 저장소와 버전 고정 Zenodo archive를 통한 aggregate
tables, figures, configuration, audit files 공개 경로가 반영되어 있다.
비공개 YouTube Analytics 원자료, 원본 영상·오디오, credentials, model
weights, runtime caches는 현재 패키지에 넣지 않았다. 저자·기관·YouTube
약관에 따른 최종 공개 범위만 확인하면 된다.

## 분석 관련 확인

- 0.05 text-event alignment threshold는 실행 설정에 고정되어 있었으나,
  현재 기록만으로 사전등록을 입증할 수 없다. 원고는 이를 명시적으로
  `not preregistered`라고 썼다.
- Figure 6의 event-control 위치 차이는 평균 normalized-position distance
  0.1918이다. 따라서 `closely matched` 또는 완벽한 위치 통제로 표현하지
  않았다. 저자가 별도 위치 매칭 가정을 주장하려면 근거가 추가로 필요하다.
- Table 7은 코드와 저장 표에서 확인된 within-video high-watch minus
  low-watch profile mean 기술 대비로 설명했다. 이를 causal effect, viewer
  state, 또는 primary association의 강건성 증거로 승격하면 안 된다.

## 영향

위 저자 확인 항목은 PDF 컴파일을 막지는 않지만, 현재 파일은 투고용 최종본이
아닌 검토용 원고다. 데이터 공개 경로와 선언 문구를 확정하기 전에는 제출할
수 없다. 분석 수치 자체를 다시 계산해야 하는 미해결 항목은 현재 없다.
