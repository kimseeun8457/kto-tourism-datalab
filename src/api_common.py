import time
import requests

MAX_RETRIES = 3
RETRY_DELAY_SEC = 1


def call_api(url: str, params: dict) -> dict:
    """공공데이터포털 API 공통 호출 래퍼. 최대 3회 재시도(1초 간격)."""
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code != 200:
                print(f"[call_api] status_code={response.status_code}")
                print(f"[call_api] response body: {response.text}")
                last_error = Exception(f"HTTP {response.status_code}")
            else:
                return response.json()
        except Exception as e:
            print(f"[call_api] attempt {attempt}/{MAX_RETRIES} failed: {e}")
            last_error = e

        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY_SEC)

    raise last_error
