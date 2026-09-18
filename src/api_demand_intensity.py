"""지역별 관광 수요 강도 (월단위, AreaTarDemDsService)"""
from src.config import SERVICE_KEY
from src.api_common import call_api

BASE_URL = "https://apis.data.go.kr/B551011/AreaTarDemDsService"

COMMON_PARAMS = {
    "serviceKey": SERVICE_KEY,
    "MobileOS": "ETC",
    "MobileApp": "HolidayBoost",
    "_type": "json",
}


def get_mobility_intensity(base_ym: str, area_cd: str, signgu_cd: str = None, tar_sjrn_ds_ix_cd: str = None) -> dict:
    """타권역방문자비중/숙박비중/숙박일수별방문자수 (areaTarSjrnDsList)"""
    url = f"{BASE_URL}/areaTarSjrnDsList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if tar_sjrn_ds_ix_cd:
        params["tarSjrnDsIxCd"] = tar_sjrn_ds_ix_cd
    return call_api(url, params)


def get_expenditure_intensity(base_ym: str, area_cd: str, signgu_cd: str = None, tar_exp_ds_ix_cd: str = None) -> dict:
    """외지인소비액/소비비중/방문량대비소비액 (areaTarExpDsList)"""
    url = f"{BASE_URL}/areaTarExpDsList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if tar_exp_ds_ix_cd:
        params["tarExpDsIxCd"] = tar_exp_ds_ix_cd
    return call_api(url, params)
