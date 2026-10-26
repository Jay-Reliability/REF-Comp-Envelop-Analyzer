# Comp Envelop Analyzer V3.0 ⚡

냉장고/에어컨 컴프레서(Linear 및 Inverter Compressor) 신뢰성 시험 데이터를 분석하고, 운전 압력(Ps vs Pd) Envelop 특성을 시각화·판정하는 웹 애플리케이션입니다.

---

## 📌 주요 기능

1. **대용량 CSV 파일 고속 로드 & 스트리밍 파싱**
   - UTF-8 및 CP949(EUC-KR) 인코딩 자동 감지
   - 2행 설명 라벨 자동 인식 및 컬럼 표준화
   - 파일 요약(컬럼별 데이터 타입, 결측치, 중복 여부) 통계 제공

2. **Linear / Inverter Comp 지능형 분석**
   - Comp 유형별 주요 센서 컬럼 자동 매핑 (Time, Power, Freq, F-Heater, C-Fan, FEI, REI, HL, 3WayValve)
   - 운전 주파수/소비전력 유효 구간 필터링 및 Envelop 규격 영역(Pass/Fail) 자동 판정
   - 제상 직후 초기 기동 구간(`1st_Comp_Defrost`) 및 Door Open 구간 Fail 자동 분리

3. **고해상도 Canvas 시각화 & Matplotlib 스타일 내비게이션**
   - 11:8 종횡비 Envelop 다이어그램 렌더링
   - 줌(Zoom), 팬(Pan), 초기화(Home), 뷰 이력 이동(Back/Forward) 지원
   - 마우스 커서 위치에 따른 실시간 Ps, Pd 좌표 표시
   - 분석 그래프 고해상도 JPG 이미지 저장 기능

4. **결과 분석 및 데이터 내보내기**
   - 20,000행 대용량 데이터 고속 가상 스크롤(Virtual Scroll) 테이블 제공
   - Envelop Dashboard 요약 CSV 내보내기
   - 판정 결과 포함 전체 분석 데이터셋 CSV 내보내기

---

## 📂 파일 구조

```text
├── 02_Envelop_Web.html      # Envelop 분석 웹 애플리케이션 원본 소스
├── app.py                   # Streamlit 호스팅 래퍼 스크립트
├── requirements.txt         # Streamlit 의존성 목록
└── README.md                # 저장소 가이드 문서