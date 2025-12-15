from pathlib import Path
from urllib.parse import urljoin

ROOT_URL = "https://geocoding.geo.census.gov/geocoder"

PROFILE = {
    "BASE_URL": urljoin(ROOT_URL) + "/",
    "PARAMETERS": {
        "layers": "54", # congress district,
        "searchtype": "onelineaddress", # see readme
        "returntype": "geographies", # prob something else needed but tbd.
    }
}