# FDTM Markdown 변환 독립 검수

- 판정: PASS_RECOMMENDED (변환 충실도 범위)
- 검수 범위: DOCX→Markdown 변환 충실도. 법령·훈련 내용 재검증 및 인가 판단 제외.
- 원고: FDTM Rev.02 수정안(검토중), 변환본 스냅샷 2
- DOCX SHA256: 722280c58b2b329733e8ca6c5864a44add5ac7d232ae5d1ddf575ec5468dd67f
- Markdown SHA256: a0a9beb93f73d955fd785f9a913ed1ceaf090887cd6515f1f6fb6c0770fa780d

원문 XML 직접 대조 결과 텍스트 노드 2,460개 누락 0, 표 44개 및 행 수·셀 텍스트 보존, 원문 제목 104개와 Markdown H2~H4 계층 매핑 일치. 목차는 표준 Markdown 중첩 목록으로 변환되었으며 숫자는 원문 목차의 기존 페이지 정보이다. Markdown 자체의 페이지·LEP는 확정하지 않았다.

## Finding FMT-001

- 분류: FORMAT_NON_COMPLIANCE
- 심각도: MEDIUM / CLOSED
- 위치: 1.2 적용 범위의 가. 아래 3개 항목 및 원문 w:pStyle a0 단락 전체
- 근거: word/styles.xml의 styleId a0 명칭은 List Bullet. word/document.xml에서 해당 스타일을 적용한 단락 확인.
- 문제: 본문 List Bullet 항목이 일반 문단으로 변환되어 목록 구조가 소실됨.
- 수정 요구: 해당 단락을 표준 Markdown 불릿(- )으로 보존. 표 내부 등 적용 맥락 확인.
- 재검증 조건: 수정본 해시 고정 후 전체 List Bullet 단락과 Markdown 목록 항목 일대일 대조, 텍스트 및 표 보존 재확인.

이 판정은 사람 또는 당국의 승인을 의미하지 않는다. 이후 변경은 재검수가 필요하다.

## 재검수 결과

수정본 스냅샷 2에서 원문 List Bullet 계열(a0/20/30) 146개 단락 모두 Markdown 불릿으로 보존됨을 독립 대조하였다. 텍스트 노드 누락 0, 표 44개 보존을 다시 확인하였다. FMT-001 CLOSED. 변환 범위의 차단 결함 없음. 법적 적합성·운영 승인·최종 인쇄 페이지 적합성은 이 검수의 대상이 아니다.
