"""지역별 관광 다양성 (월단위, AreaTarDivService)"""
from src.config import SERVICE_KEY
from src.api_common import call_api

BASE_URL = "https://apis.data.go.kr/B551011/AreaTarDivService"

COMMON_PARAMS = {
    "serviceKey": SERVICE_KEY,
    "MobileOS": "ETC",
    "MobileApp": "HolidayBoost",
    "_type": "json",
}


def get_tourist_diversity(base_ym: str, area_cd: str, signgu_cd: str = None, tou_div_ix_cd: str = None) -> dict:
    """연령별 방문객수 (areaTouDivList)"""
    url = f"{BASE_URL}/areaTouDivList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if tou_div_ix_cd:
        params["touDivIxCd"] = tou_div_ix_cd
    return call_api(url, params)


def get_expenditure_diversity(base_ym: str, area_cd: str, signgu_cd: str = None, exp_div_ix_cd: str = None) -> dict:
    """연령별 소비액 (areaExpDivList)"""
    url = f"{BASE_URL}/areaExpDivList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if exp_div_ix_cd:
        params["expDivIxCd"] = exp_div_ix_cd
    return call_api(url, params)


def get_international_diversity(base_ym: str, area_cd: str, signgu_cd: str = None, intl_div_ix_cd: str = None) -> dict:
    """외국인 소비액/방문자수/국적다양성 (areaIntlDivList)"""
    url = f"{BASE_URL}/areaIntlDivList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if intl_div_ix_cd:
        params["intlDivIxCd"] = intl_div_ix_cd
    return call_api(url, params)
