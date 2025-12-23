import src.utils.typesafe_utils as t
from src.classes.fetcher import Fetcher

from src.utils.misc_utils import centroid_to_lon_lat


class Tigerweb:

    def __init__(self, fetcher=None):
        if not fetcher:
            self.f: Fetcher = Fetcher(
                {
                    "BASE_URL": "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/",
                }
            )


    def get_tigerweb_zip_to_centroid(self, zcta5: str) -> tuple[int, int]:
        " returns the centroid of a zip area in lon, lat"
        params = {
            'where': f"ZCTA5='{zcta5}'",
            'returnExtentOnly': 'true',
            'returnGeometry': 'false',
            'f': 'json',
        }

        response = self.f.get(
            "2/query",
            params=params
        )

        if isinstance(response.content, dict):

            centroid_vals = t.dig(response.content, ["extent"])
            response = centroid_to_lon_lat(
                t.dig(centroid_vals, ['xmin']), 
                t.dig(centroid_vals, ['xmax']), 
                t.dig(centroid_vals, ['ymin']), 
                t.dig(centroid_vals, ['ymax']),
            )

            return response

        return response.content
    

    def get_congressional_district_from_centroid(self, lon:int , lat: int) -> dict:
        """ returns a list of features: which are the congressional districts in the area? """
        params = {
            "geometry": f"{lon},{lat}",          # lon,lat
            "geometryType": "esriGeometryPoint",
            "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "STATE,CD119,NAME,GEOID", # TODO: make this dynamic for current class of congress
            "returnGeometry": "false",
            "f": "json",
        }

        response = self.f.get(
            "54/query",
            params=params
        )


        return response.content

if __name__ == "__main__":
    tiger_fetcher = Tigerweb()
    response = tiger_fetcher.get_tigerweb_zip_to_centroid("11211")

    district_info = tiger_fetcher.get_congressional_district_from_centroid(*response)

    print(district_info)
