import math


def centroid_to_lon_lat(xmin: int, xmax:int, ymin:int, ymax:int):

    # center of the extent (EPSG:3857 / Web Mercator meters)
    x = (xmin + xmax) / 2.0
    y = (ymin + ymax) / 2.0

    # Web Mercator (3857) -> lon/lat (4326)
    R = 6378137.0
    lon = (x / R) * 180.0 / math.pi
    lat = (2.0 * math.atan(math.exp(y / R)) - math.pi / 2.0) * 180.0 / math.pi

    return lon, lat



def fips_to_abbr(state_fips):
    if not state_fips:
        return None
    
    FIPS_TO_ABBR = {
        "01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO",
        "09": "CT", "10": "DE", "11": "DC", "12": "FL", "13": "GA", "15": "HI",
        "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY",
        "22": "LA", "23": "ME", "24": "MD", "25": "MA", "26": "MI", "27": "MN",
        "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH",
        "34": "NJ", "35": "NM", "36": "NY", "37": "NC", "38": "ND", "39": "OH",
        "40": "OK", "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD",
        "47": "TN", "48": "TX", "49": "UT", "50": "VT", "51": "VA", "53": "WA",
        "54": "WV", "55": "WI", "56": "WY",
    }
    abbr = FIPS_TO_ABBR[state_fips.zfill(2)]

    return abbr