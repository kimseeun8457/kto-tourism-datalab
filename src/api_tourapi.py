"""국문 관광정보서비스 (TourAPI, KorService2)

한국관광공사_개방데이터_활용매뉴얼(국문)_v4.4.docx 기준.
v4.4부터 지역 필터는 구(舊) areaCode/sigunguCode가 아니라
법정동 코드 기반 lDongRegnCd(시도)/lDongSignguCd(시군구)를 사용한다.
"""
from src.config import SERVICE_KEY
from src.api_common import call_api

BASE_URL = "http://apis.data.go.kr/B551011/KorService2"

COMMON_PARAMS = {
    "serviceKey": SERVICE_KEY,
    "MobileOS": "ETC",
    "MobileApp": "HolidayBoost",
    "_type": "json",
}


def get_area_based_list(
    l_dong_regn_cd: str,
    l_dong_signgu_cd: str = None,
    content_type_id: str = None,
    page_no: int = 1,
    num_of_rows: int = 100,
    arrange: str = "C",
) -> dict:
    """지역(시도/시군구) 기준 관광지 목록 조회 (areaBasedList2)"""
    url = f"{BASE_URL}/areaBasedList2"
    params = {
        **COMMON_PARAMS,
        "lDongRegnCd": l_dong_regn_cd,
        "pageNo": page_no,
        "numOfRows": num_of_rows,
        "arrange": arrange,
    }
    if l_dong_signgu_cd:
        params["lDongSignguCd"] = l_dong_signgu_cd
    if content_type_id:
        params["contentTypeId"] = content_type_id
    return call_api(url, params)
