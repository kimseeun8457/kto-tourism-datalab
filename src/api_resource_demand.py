"""지역별 관광 자원 수요 (월단위, AreaTarResDemService)"""
from src.config import SERVICE_KEY
from src.api_common import call_api

BASE_URL = "https://apis.data.go.kr/B551011/AreaTarResDemService"

COMMON_PARAMS = {
    "serviceKey": SERVICE_KEY,
    "MobileOS": "ETC",
    "MobileApp": "HolidayBoost",
    "_type": "json",
}


def get_tourism_service_demand(base_ym: str, area_cd: str, signgu_cd: str = None, tar_svc_dem_ix_cd: str = None) -> dict:
    """SNS언급량/업종별소비액/내비게이션 숙박·음식·쇼핑 검색량 (areaTarSvcDemList)"""
    url = f"{BASE_URL}/areaTarSvcDemList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if tar_svc_dem_ix_cd:
        params["tarSvcDemIxCd"] = tar_svc_dem_ix_cd
    return call_api(url, params)


def get_cultural_resource_demand(base_ym: str, area_cd: str, signgu_cd: str = None, cul_res_dem_ix_cd: str = None) -> dict:
    """내비게이션 문화·레저·역사·체험·자연관광 검색량 (areaCulResDemList)"""
    url = f"{BASE_URL}/areaCulResDemList"
    params = {**COMMON_PARAMS, "baseYm": base_ym, "areaCd": area_cd}
    if signgu_cd:
        params["signguCd"] = signgu_cd
    if cul_res_dem_ix_cd:
        params["culResDemIxCd"] = cul_res_dem_ix_cd
    return call_api(url, params)
