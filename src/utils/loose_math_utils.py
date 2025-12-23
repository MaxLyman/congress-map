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