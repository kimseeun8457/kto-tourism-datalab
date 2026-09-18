"""특일정보 (한국천문연구원, SpcdeInfoService)

주의: 이 API만 다른 5개 API와 파라미터 네이밍 컨벤션이 다르다.
- serviceKey (X) -> ServiceKey (대문자 S)
- startYmd/baseYm (X) -> solYear, solMonth
"""
from src.config import SERVICE_KEY
from src.api_common import call_api

BASE_URL = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService"

COMMON_PARAMS = {
    "ServiceKey": SERVICE_KEY,
    "_type": "json",
}


def get_holiday_info(sol_year: str, sol_month: str, num_of_rows: int = 30) -> dict:
    """공휴일 정보조회 (getRestDeInfo)"""
    url = f"{BASE_URL}/getRestDeInfo"
    params = {
        **COMMON_PARAMS,
        "solYear": sol_year,
        "solMonth": sol_month,
        "numOfRows": num_of_rows,
    }
    return call_api(url, params)


def get_national_holiday_info(sol_year: str, sol_month: str, num_of_rows: int = 30) -> dict:
    """국경일 정보조회 (getHoliDeInfo)

    isHoliday=N인 항목도 섞여 나올 수 있음(예: 제헌절).
    실제 공휴일 캘린더 구축 시에는 isHoliday == 'Y'인 것만 필터링해서 사용할 것.
    """
    url = f"{BASE_URL}/getHoliDeInfo"
    params = {
        **COMMON_PARAMS,
        "solYear": sol_year,
        "solMonth": sol_month,
        "numOfRows": num_of_rows,
    }
    return call_api(url, params)


def get_holidays_range(start_year: int, start_month: int, end_year: int, end_month: int) -> list:
    """start_year/start_month ~ end_year/end_month까지 월단위로 반복 호출하여 공휴일 정보 수집"""
    results = []
    year, month = start_year, start_month
    while (year, month) <= (end_year, end_month):
        sol_year = str(year)
        sol_month = f"{month:02d}"
        data = get_holiday_info(sol_year, sol_month)
        try:
            items = data["response"]["body"]["items"]
            if items:
                item = items["item"]
                if isinstance(item, dict):
                    item = [item]
                results.extend(item)
        except (KeyError, TypeError):
            print(f"[get_holidays_range] {sol_year}-{sol_month} 응답 파싱 실패: {data}")

        month += 1
        if month > 12:
            month = 1
            year += 1

    return results
