from pathlib import Path
from urllib.parse import urljoin


API_VERSION = "v3"
ROOT_URL = "https://api.congress.gov/"
CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "api_congress_gov.ini"

PROFILE = {
    "BASE_URL": urljoin(ROOT_URL, API_VERSION) + "/",
    "CONFIG_PATH": CONFIG_PATH, 
    "KEY_NAME": "x-api-key",
}