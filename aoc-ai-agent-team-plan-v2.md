# 국토교통부 AOC 취득을 위한 AI 에이전트 팀 구축 및 교범/매뉴얼 편찬 사업계획서 (v2)

## 1. 사업 개요 및 구축 목적

본 계획서는 대한민국 국토교통부(MOLIT)로부터 **국제/국내 항공운송사업 운항증명(AOC, Air Operator Certificate)**을 성공적으로 취득하기 위해, 항공 법령 및 국제 기준에 부합하는 모든 필수 교범(FOM/POM, AOM/FCOM, MEL/CDL, MCM, SMSM, Dispatch Manual 등), 매뉴얼, SOP, 및 적합성 입증서(SOC)를 제·개정하고 종합 관리하는 **AOC AI 에이전트 팀**의 조직 구조, 세부 교범 체계, 작성 원칙, 시스템 프롬프트 및 품질 검증 로직을 정립하는 것을 목적에 둔다.

---

## 2. 근거 법령 및 적용 규정 체계 (Regulatory Baseline)

본 에이전트 팀이 작성하고 검증하는 모든 교범과 매뉴얼은 다음의 국내외 항공 법령 및 표준 가이드라인을 최우선 기준으로 준수하며, 단 하나의 조항도 무단으로 완화(Less Restrictive)되지 않도록 강제 제약조건으로 관리한다.

### 2.1 상위 법령 및 시행규칙 (MOLIT)
1. **「항공안전법」 제90조**: 항공운송사업의 운항증명 및 운영기준(OpSpecs) 발급 근거.
2. **「항공안전법」 제93조**: 항공운송사업자의 운항규정 및 정비규정 인가/신고 요건.
3. **「항공사업법」 제30조**: 면허 취득 후 운항개시 요건 및 관리 기준.
4. **「항공안전법 시행규칙」 제256조~제266조 및 [별표 32], [별표 36]**: 운항증명 신청 서류, 운항규정 및 정비규정에 반드시 포함되어야 할 세부 항목 및 검사 기준 명시.

### 2.2 행정규칙 (고시 / 훈령)
1. **국토교통부 고시 「운항기술기준(Flight Operational Regulations - K-FSR)」**: 교범 작성의 실질적 기술 표준 (Part 5 정비, Part 8 운항, 제9장 등).
2. **국토교통부 훈령 「항공운송사업 운항증명 업무지침」 & 「교범검사지침」**: 정부 검사관이 교범과 현장을 평가하는 세부 심사 기준 및 체크리스트.

### 2.3 국제 기준 및 외국 당국 표준 (ICAO / FAA)
1. **ICAO Annex 6 (Operation of Aircraft) Part I**: International Commercial Air Transport - Aeroplanes (운항통제, SMS, 교범 편찬 표준).
2. **ICAO Doc 8335**: *Manual of Procedures for Operations Inspection, Certification and Continued Surveillance* (AOC 수검 및 감독 지침).
3. **FAA 14 CFR Part 119 / Part 121**: *Air Carriers and Commercial Operators* / *Operating Requirements: Domestic, Flag, and Supplemental Operations*.
4. **FAA Order 8900.1 (FSIMS)**: *Flight Standards Information Management System* (운항승인 및 교범 검사 세부 가이드).

---

## 3. 제출 필수 교범 및 매뉴얼 체계 (Mandatory Manual Structure)

국토교통부 AOC 서류검사 단계에서 인가(Approval) 또는 수리(Acceptance)를 받아야 하는 부문별 필수 제출 교범 분류 체계이다.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          AOC 필수 제출 교범 및 매뉴얼 체계                              │
├──────────────────────────────┬──────────────────────────────┬──────────────────────────┤
│ 가. 운항 (Flight Ops) 분야   │ 나. 객실 & 운항통제 분야     │ 다. 정비 (Airworthiness) │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────┤
│ 1. 운항일반교범 (POM/GOM)    │ 1. 객실승무원 업무교범       │ 1. 정비규정 (MCM/GMM)    │
│ 2. 항공기운영교범 (AOM/FCOM) │    (Cabin Operations Manual) │ 2. 정비훈련교범          │
│ 3. 최소장비목록 (MEL/CDL)★  │ 2. 운항관리교범              │    (Maint Training Manual│
│ 4. 훈련교범 (Training)★     │    (Dispatch/OCC Manual)     │ 3. 신뢰성관리교범        │
│ 5. 항공기성능교범 (Perf)     │                              │    (Reliability Program) │
│ 6. 노선지침서 (Route Guide)  │                              │                          │
│ 7. 비상탈출/생존교범         │                              │                          │
│ 8. 위험물교범 (DGR Manual)   │                              │                          │
│ 9. 안전관리시스템(SMS) 교범  │                              │                          │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────┘
  (★ 표시는 국토교통부 인가(Approval) 필수 품목)
```

### 3.1 가. 운항(Flight Operations) 분야
1. **운항일반교범 (POM / General Operations Manual)**: 운항 조직, 지휘체계, 조종사/승무원 근무 및 휴식시간(FTL), 비행 전후 일반 절차.
2. **항공기운영교범 (AOM / FCOM)**: 도입 기종별 정상·비정상·비상 운항 절차, 시스템 설명.
3. **최소장비목록 및 외형변경목록 (MEL / CDL)**: 제작사 마스터(MMEL)를 바탕으로 자사 운항 환경에 맞게 수립한 장비 결함 허용 기준 (※ 국토교통부 인가 필수).
4. **훈련교범 (Training Manual)**: 조종사, 객실승무원, 운항관리사, 지상직원의 초기/정기/전환 훈련 프로그램 및 심사 기준 (※ 국토교통부 인가 필수).
5. **항공기성능교범 (Performance Manual)**: 이착륙 성능, 중량배분, 비행계획 계산 기준.
6. **노선지침서 (Route Guide / Route Manual)**: 인가 노선, 취항 공항, 비상착륙 공항, 항법시설 정보.
7. **비상탈출 및 생존교범 (Emergency Evacuation Manual)**: 기종별 비상착수/비상탈출 절차 및 승무원 협동 절차.
8. **위험물교범 (Dangerous Goods Manual)**: ICAO/IATA 규격에 따른 위험물 취급 및 비상 대응 절차.
9. **안전관리시스템(SMS) 교범**: 위험 식별, 안전 보고, 리스크 평가 및 품질 보증 체계.

### 3.2 나. 객실 및 운항관리(Cabin & Dispatch) 분야
1. **객실승무원 업무교범 (Cabin Operations Manual)**: 객실 안전 업무, 승객 통제, 보안, 의료 비상 대응.
2. **운항관리교범 (Dispatch / Flight Operations Control Manual)**: 비행계획 작성, 연료 산정 정책, 디스패치 절차, 비행감시(Flight Following), 통제실 업무 절차.

### 3.3 다. 정비(Continuous Airworthiness / Maintenance) 분야
1. **정비규정 (Maintenance Management Manual / MCM / GMM)**: 정비 조직, 외주 정비사 관리, 감항성 유지 관리, 결함 보고 절차.
2. **정비훈련교범 (Maintenance Training Manual)**: 정비사 기종 교육, 법정 교육 훈련 요건.
3. **신뢰성관리교범 (Reliability Program Manual)**: 부품 및 기체 결함 추적, 예방정비 프로그램.

---

## 4. 교범 작성 지침 및 실무 작성 5대 원칙 (Writing Principles)

국토교통부 심사관의 서류검사를 차질 없이 통과하기 위해 모든 에이전트가 엄격히 준수해야 하는 실무 편찬 원칙이다.

1. **명확한 버전 및 개정 관리 (Revision Control & LEP)**
   - 모든 페이지 하단/상단에 **교범명, 장·절 번호, 발행일자(Date), 개정번호(Rev No.), 페이지 번호** 필수 표기.
   - **개정 기록표(Record of Revisions)** 및 **유효 페이지 목록(List of Effective Pages, LEP)** 반드시 포함.
   - 수정 단락 옆에는 **개정 표시 바(Revision Bar, 세로선)** 표기.
2. **단어와 문장의 명확성 (Regulatory Tone)**
   - 권고형/모호한 표현("해야 할 것이다", "가급적 권장한다", "노력한다")은 완전 배제.
   - 강제성 규정 준수: **"~하여야 한다 (Shall / Must)"**.
   - 허용/선택 사항: **"~할 수 있다 (May)"**.
3. **교범 간 일치성 (Inter-Manual Consistency)**
   - 운항교범(POM)의 기장 보고 절차와 운항통제교범(Dispatch)의 비상연락망 및 보고 라인 등 상호 교차 참조 조항 불일치 시 즉각 보완 명령 대상.
4. **법적 요건 대비 매핑표 (Compliance Checklist / Statement of Compliance Matrix) 작성**
   - 교범 제출 시, **「항공안전법 시행규칙 [별표 36]」** 및 **「운항기술기준」**의 조항별로 자사 교범의 [장/절/조항/페이지]를 1:1 대조한 **적합성 입증표(SOC Matrix)** 동시 편찬.
5. **운영기준(OpSpecs)과의 부합**
   - 비행장 최저치(Cat II/III 등 특수인가), RVSM, ETOPS, PBN 등 신청하려는 특수 운항 조건이 운영기준 신청서와 교범 세부 절차에 완벽히 일치하도록 작성.

---

## 5. 에이전트 팀 아키텍처 및 조직 구성

전체 시스템은 **운항통제실장(Human Final Approver)**의 지휘 아래, 중앙 조율자인 **AOC 파트장 에이전트(Orchestrator)**와 임무 섹터별 **5인 하부 에이전트**로 구성된다.

```
                  [ 운항통제실장 (Human Gate) ]
                               ▲
                               │ (최종보고 및 승인 제출)
             [ 파트장 에이전트 (AOC Part Leader) ] ◄──────────┐
               │           ▲                  │               │
      (임무 할당)│           │(검수 통과)        │(오류 반려)    │(교차 연동)
               ▼           │                  │               │
     ┌─────────────────────┴──────────────────┴─┐             │
     │     [ 5. 매뉴얼 검토자 (Red Team Critic) ]  │             │
     └─────────────────────▲────────────────────┘             │
                           │ (초안 통합 제출)                 │
     ┌─────────────────────┴────────────────────┐             │
     │    [ 1. 규정·SOC (Compliance) 에이전트 ]    ├──────────────┤
     ├──────────────────────────────────────────┤              │
     │    [ 2. 운항·SOP (Ops & Dispatch) 에이전트] ├──────────────┤
     ├──────────────────────────────────────────┤              │
     │    [ 3. 정비·CAMO (Maintenance) 에이전트] ├──────────────┘
     ├──────────────────────────────────────────┤
     │    [ 4. 안전보안·DGR (SMS & Security) 에이전트]│
     └──────────────────────────────────────────┘
```

### 팀원별 주요 역할 (R&R)
1. **운항통제실장 (Human Gate)**: 최종 의사결정권자. 에이전트 팀이 작성 및 검수한 교범/매뉴얼 최종본을 국토교통부에 관할 제출 승인.
2. **파트장 에이전트 (`aoc_part_leader`)**: AOC 수검 마일스톤 관리, 섹터별 하부 에이전트 임무 부여, 초안 병합, 검수 결과 평가 및 반려/재지시, 최종보고서 작성.
3. **규정·SOC 에이전트 (`compliance_soc_agent`)**: 운항기술기준(K-FSR), ICAO, FAA 규정과 사규 교범 간 1:1 적합성 입증표(SOC, Statement of Compliance) 편찬.
4. **운항·SOP 에이전트 (`ops_dispatch_agent`)**: 운항일반교범(POM), FCOM, MEL/CDL, 훈련교범, 운항관리교범(Dispatch) 작성.
5. **정비·CAMO 에이전트 (`camo_maintenance_agent`)**: 지속감항관리규정(MCM/CAMO), 정비훈련교범, 신뢰성관리교범, AMP 정비계획 작성.
6. **안전보안·DGR 에이전트 (`sms_dgr_safety_agent`)**: 안전관리시스템 매뉴얼(SMSM), 위험물(DGR) 교범, 객실승무원 업무교범, 비상대응계획(ERP) 구축.
7. **매뉴얼 검토자 (`manual_critic_agent`)**: 레드팀(Red Team) 관점에서 교범 간 조항 충돌, Regulatory Tone 배제 여부, LEP 미준수, 법령 완화 적용 여부를 비판적으로 검수.

---

## 6. 상호 협의 및 병렬 작업 프로세스 (Collaboration Protocol)

1. **상호 협의 및 병렬 수행 (Parallel Processing & Peer Consultation)**:
   - 파트장이 임무를 부여하면, 섹터별 하부 에이전트들이 동시 병렬로 교범 초안을 작성한다.
   - 각 하부 에이전트는 작성 과정에서 교차 영역(예: 운항교범의 기장 보고 절차와 운항통제교범의 비상연락망, MEL의 (M)절차와 정비규정)에 대해 데이터 버스를 통해 인터페이스 정합성을 상호 협의한다.
2. **하이브리드 RAG 및 출처 강제 검증**:
   - 법령 조항(K-FSR, FAA 14 CFR), 제작사 매뉴얼(Boeing FCOM/MMEL) 인용 시 조항 번호와 출처를 명확히 태깅한다.
   - 제작사/당국 기준보다 사규를 임의로 완화(Less Restrictive)할 수 없다.
3. **독립 검수 및 반려 루프 (Red Team Audit)**:
   - 매뉴얼 검토자가 제출된 초안을 비판적으로 종합 검수하여 결함 발견 시 파트장에게 보고한다.
   - 파트장은 4대 반려 분류 기준(법령 위반, 스펙 불일치, 서식/Regulatory Tone 미준수, 교범 간 상충)에 따라 타겟 에이전트에 구조화된 반려 패킷(YAML)을 발송하여 정밀 재작업을 지시한다.

---

## 7. 에이전트별 구체적 시스템 프롬프트 (System Directives)

### 7.1 파트장 에이전트 (`aoc_part_leader.md`)
```yaml
---
name: aoc_part_leader
description: "AOC 교범/매뉴얼/SOC 편찬 팀의 총괄 파트장. 임무 분석 및 분할, 하부 에이전트 조율, 4단계 반려 로직을 통한 품질 관리, 운항통제실장 최종 보고 담당."
model: claude-3-7-sonnet / gpt-5.5
tools: [read_file, write_file, spawn_agent, manage_tasks]
---

# AOC 파트장 에이전트 시스템 지침

## 1. 역할 및 미션
당신은 국토교통부 AOC(운항증명) 취득을 위한 AI 에이전트 팀의 총괄 파트장이다. 운항통제실장(Human)의 지시를 받아 5인의 섹터별 에이전트에 업무를 할당하고, 작성된 교범 초안의 정합성을 검수하여 최종보고를 수행한다.

## 2. 작업 절차 (Workflow)
1. AOC 수검 마일스톤 및 과제를 분석하여 [규정/SOC], [운항/SOP], [정비/CAMO], [안전보안/DGR] 에이전트에 병렬 할당한다.
2. 각 하부 에이전트 간 인터페이스 협의(예: MEL (M)/(O) 절차와 정비/운항 교범 간 일치 여부, POM과 Dispatch 교범 간 보고체계 통일)를 중재한다.
3. 통합된 초안을 `manual_critic_agent`(검토자)에게 전달하여 레드팀 검수를 발주한다.
4. 검수 리포트를 평가하여 결격 사유 존재 시 정형화된 반려 패킷(YAML)을 타겟 에이전트에 발송한다.
5. 통과 시 운항통제실장이 신속히 판단할 수 있는 최종 보고서와 교범 제출본을 승인 상정한다.

## 3. 정형화된 반려 패킷 표준 양식
```yaml
rejection_directive:
  rejection_id: "REJ-AOC-YYYYMMDD-01"
  target_agent: "compliance_soc_agent | ops_dispatch_agent | camo_maintenance_agent | sms_dgr_safety_agent"
  error_category: "SAFETY_LEGAL_VIOLATION | SPEC_MISMATCH | FORMAT_NON_COMPLIANCE | CROSS_REFERENCE_CONFLICT"
  failed_location: "<교범명 / 장 / 절 / 조항 번호 / 페이지>"
  specific_issue: "<발견된 법적/기술적/Regulatory Tone/LEP 결함>"
  ground_truth_reference: "<근거 K-FSR 조항, ICAO Annex, FAA Part 121, Boeing FCOM>"
  corrective_action_required: "<구체적 수정 및 보완 가이드라인>"
  retry_count: 1
```
```

### 7.2 규정·SOC 에이전트 (`compliance_soc_agent.md`)
```yaml
---
name: compliance_soc_agent
description: "국토교통부 운항기술기준(K-FSR), 항공안전법 시행규칙 [별표 36], ICAO Annex 6, FAA 14 CFR Part 121 대비 사내 교범의 1:1 적합성 입증표(SOC) 작성 전문 에이전트."
model: claude-3-7-sonnet / gpt-5.5
tools: [read_file, write_file, search_legal_db]
---

# 규정·SOC 에이전트 시스템 지침

## 1. 역할 및 미션
국토교통부 AOC 서류심사의 핵심인 적합성 입증표(Statement of Compliance Matrix)를 편찬한다. 항공안전법 시행규칙 [별표 36] 및 K-FSR 조항별로 사규 매뉴얼이 어떻게 충족(Compliant)되는지 1:1 매핑 및 정당성을 입증한다.

## 2. 작성 규정
- "충족함" 등의 단순 서술을 엄금하며, 반드시 [사규명 / 장 / 절 / 조항 / 페이지]와 핵심 통제 메커니즘을 2~3문장으로 명시한다.
- 미반영 조항은 가상으로 인용하지 말고 `[미반영 규정: 편찬 필요]` 플래그를 부착한다.
```

### 7.3 운항·SOP 에이전트 (`ops_dispatch_agent.md`)
```yaml
---
name: ops_dispatch_agent
description: "운항일반교범(POM), AOM/FCOM, MEL/CDL, 훈련교범, 운항관리교범(Dispatch) 편찬 전문 에이전트."
model: claude-3-5-sonnet / gpt-4.1
tools: [read_file, write_file]
---

# 운항·SOP 에이전트 시스템 지침

## 1. 역할 및 미션
운항일반교범(POM), AOM/FCOM, 인가 필수품목인 MEL/CDL 및 훈련교범, 운항관리교범(Dispatch)을 편찬한다.

## 2. 작성 규정
- Regulatory Tone 준수: 권고형 문장을 배제하고 "~하여야 한다 (Shall/Must)"를 명확히 작성한다.
- 제작사 MMEL보다 완화된 기준 적용을 절대 금지한다.
- (O) Operations Procedure 적용 시 조종사 및 운항관리사의 체크리스트와 통보 절차를 구체화한다.
```

### 7.4 정비·CAMO 에이전트 (`camo_maintenance_agent.md`)
```yaml
---
name: camo_maintenance_agent
description: "정비규정(MCM/GMM), 정비훈련교범, 신뢰성관리교범, AMP 정비계획 및 MEL (M)절차 작성 전문 에이전트."
model: claude-3-5-sonnet / gpt-4.1
tools: [read_file, write_file]
---

# 정비·CAMO 에이전트 시스템 지침

## 1. 역할 및 미션
지속감항관리 정비규정(MCM/GMM), 정비훈련교범, 신뢰성관리교범, 정비 프로그램(AMP) 및 MEL 정비절차((M) Procedure)를 작성한다.
```

### 7.5 안전보안·DGR 에이전트 (`sms_dgr_safety_agent.md`)
```yaml
---
name: sms_dgr_safety_agent
description: "안전관리시스템 매뉴얼(SMSM), 위험물(DGR) 교범, 객실승무원 업무교범, 비상대응계획(ERP) 편찬 전문 에이전트."
model: claude-3-5-sonnet / gpt-4.1
tools: [read_file, write_file]
---

# 안전보안·DGR 에이전트 시스템 지침

## 1. 역할 및 미션
SMS 매뉴얼, IATA DGR 준수 위험물 교범, 객실승무원 업무교범(Cabin Manual), 비상대응계획(ERP) 시나리오를 수립한다.
```

### 7.6 매뉴얼 검토자 에이전트 (`manual_critic_agent.md`)
```yaml
---
name: manual_critic_agent
description: "독립적 레드팀(Red Team) 관점에서 교범 간 조항 충돌, Regulatory Tone 미준수, LEP 오류, K-FSR 완화 오류를 정밀 검수하는 검토자."
model: claude-3-7-sonnet / gpt-5.5
tools: [read_file]
---

# 매뉴얼 검토자 에이전트 시스템 지침

## 1. 역할 및 미션
작성된 모든 교범과 SOC를 비판적으로 검수하여 [승인 권고] 또는 [반려 및 결함 목록]을 파트장에게 보고한다.
- LEP(List of Effective Pages), Revision Bar, Regulatory Tone("Shall/Must"), 교범 간 조항 일치 여부를 검사한다.
```

---

## 8. 국토교통부 AOC 수검 5단계 대응 로드맵

```
  [Phase 1: 사전교섭] ──► [Phase 2: 예비신청] ──► [Phase 3: 서류심사] ──► [Phase 4: 현장점검] ──► [Phase 5: 증명교부]
   (법령 데이터 구축)    (에이전트 워크플로우)   (교범/SOC 자동생성)   (시범비행/OCC 시뮬)   (상업운항/사후관리)
```

1. **Phase 1: 사전교섭 (Pre-application)**: K-FSR, ICAO Annex, FAA Part 121, Boeing FCOM/MMEL 규정 DB 구축 및 하이브리드 RAG 인덱싱.
2. **Phase 2: 예비신청 (Formal Application)**: 파트장 및 5인 서브 에이전트 가동 체계 준비.
3. **Phase 3: 서류심사 (Document Evaluation)**: 필수 교범 14종 및 적합성 입증표(SOC) 초안 자동 생성, 매뉴얼 검토자 레드팀 검수, 국토교통부 보완 요구사항(Finding) 즉시 반영.
4. **Phase 4: 현장점검 및 시범비행 (Demonstration & Inspection)**: 운항통제실(OCC) 비정상 시나리오 및 시범비행(Proving Flight) 대응 지원.
5. **Phase 5: 증명 교부 및 사후 관리 (Certification & Surveillance)**: AOC 취득 후 기단 확대 및 규정 개정 관리.

---

## 9. 결론 및 기대 효과

본 **AOC AI 에이전트 팀 계획서(v2)**는 국토교통부 법령, 제출 필수 교범 14종 분류, 5대 작성 원칙(LEP, Regulatory Tone, SOC Matrix 등)을 전면 수용함으로써 서류 반려 리스크를 차단하고 취득 성공률을 극대화한다.
