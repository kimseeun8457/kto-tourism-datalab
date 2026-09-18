"""지역별 방문자수 (한국관광 데이터랩 DataLabService)"""
from src.config import SERVICE_KEY
from src.api_common import call_api

BASE_URL = "http://apis.data.go.kr/B551011/DataLabService"

COMMON_PARAMS = {
    "serviceKey": SERVICE_KEY,
    "MobileOS": "ETC",
    "MobileApp": "HolidayBoost",
    "_type": "json",
}


def get_metro_visitors(start_ymd: str, end_ymd: str, page_no: int = 1, num_of_rows: int = 100) -> dict:
    """광역 지역별 방문자수 (metcoRegnVisitrDDList)"""
    url = f"{BASE_URL}/metcoRegnVisitrDDList"
    params = {
        **COMMON_PARAMS,
        "startYmd": start_ymd,
        "endYmd": end_ymd,
        "pageNo": page_no,
        "numOfRows": num_of_rows,
    }
    return call_api(url, params)


def get_local_visitors(start_ymd: str, end_ymd: str, page_no: int = 1, num_of_rows: int = 100) -> dict:
    """기초 지역별 방문자수 (locgoRegnVisitrDDList)"""
    url = f"{BASE_URL}/locgoRegnVisitrDDList"
    params = {
        **COMMON_PARAMS,
        "startYmd": start_ymd,
        "endYmd": end_ymd,
        "pageNo": page_no,
        "numOfRows": num_of_rows,
    }
    return call_api(url, params)
