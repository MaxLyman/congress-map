ROOT_URL = "https://geocoding.geo.census.gov/geocoder"

PROFILE = {
    "BASE_URL": ROOT_URL + "/",
    "PARAMETERS": {
        # NOTE: Census Geocoder uses /geocoder/{returntype}/{searchtype} in the PATH.
        # So `returntype` is NOT a query param; don't put it in PARAMETERS.
        "benchmark": 4,
        "vintage": "Current_Current",
        "layers": "54",  # 119th Congressional Districts (Current service)
    }
}