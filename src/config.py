from dotenv import load_dotenv
import os

load_dotenv()
SERVICE_KEY = os.getenv("DATA_GO_KR_SERVICE_KEY")

if not SERVICE_KEY:
    raise ValueError("DATA_GO_KR_SERVICE_KEY가 .env 파일에 설정되지 않았습니다.")
