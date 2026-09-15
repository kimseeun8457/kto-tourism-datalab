# HOLIDAY BOOST

공휴일이 지역 관광 방문에 미치는 효과(Holiday Lift)를 분석하여, 공휴일 효과가 큰 성공지역과 아직 드러나지 않은 잠재지역을 찾아내는 프로젝트.

## 핵심 질문
공휴일이 평시 대비 방문객 수를 얼마나 끌어올리는가(Holiday Lift), 그리고 그 효과가 큰 지역/잠재지역은 어디인가?

## 분석 파이프라인

- STEP 0: 데이터 수집 (한국관광 데이터랩 다운로드)
- STEP 1: 공휴일 캘린더 정리
- STEP 2: 원본 데이터 클리닝 및 전처리
- STEP 3: 지역별 평시 방문 데이터 정의
- STEP 4: 공휴일 기간 방문 데이터 집계
- STEP 5: Holiday Lift 지표 계산
- STEP 6: 지역별 Holiday Lift 랭킹
- STEP 7: 성공지역 기준 적용 및 필터링
- STEP 8: 잠재지역 평가 변수 산출
- STEP 9: 스코어링 및 최종 지역 선정
- STEP 10: 결과 시각화 및 리포트 정리

## 폴더 구조

| 경로 | 설명 |
|---|---|
| `data/raw/` | 데이터랩에서 다운로드한 원본 (csv/xlsx) |
| `data/processed/` | 전처리된 중간 산출물 |
| `notebooks/` | 분석 단계별 노트북 (step1_calendar.ipynb 등) |
| `src/` | 재사용 함수 (holiday_lift 계산 등) |
| `outputs/figures/` | 그래프 이미지 |
| `outputs/tables/` | 최종 표 (성공지역/잠재지역 리스트 등) |
| `docs/` | 분석 가이드라인, 노션 정리 문서 백업 |

## 사용 스택
- Python (pandas, matplotlib/plotly)
- 데이터 출처: 한국관광 데이터랩 (datalab.visitkorea.or.kr)
