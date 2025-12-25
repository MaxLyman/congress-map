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
        """
        [Layer: 2020 Census ZIP Code Tabulation Areas (ID: 2)] (https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/2)
        OID ( type: esriFieldTypeString, alias: OID, length: 22 )
        ZCTA5 ( type: esriFieldTypeString, alias: ZCTA5, length: 5 )
        GEOID ( type: esriFieldTypeString, alias: GEOID, length: 5 )
        BASENAME ( type: esriFieldTypeString, alias: BASENAME, length: 100 )
        LSADC ( type: esriFieldTypeString, alias: LSADC, length: 2 )
        NAME ( type: esriFieldTypeString, alias: NAME, length: 100 )
        MTFCC ( type: esriFieldTypeString, alias: MTFCC, length: 5 )
        ZCTA5CC ( type: esriFieldTypeString, alias: ZCTA5CC, length: 2 )
        FUNCSTAT ( type: esriFieldTypeString, alias: FUNCSTAT, length: 1 )
        AREALAND ( type: esriFieldTypeString, alias: AREALAND, length: 20 )
        AREAWATER ( type: esriFieldTypeString, alias: AREAWATER, length: 20 )
        STGEOMETRY ( type: esriFieldTypeGeometry, alias: STGEOMETRY )
        CENTLAT ( type: esriFieldTypeString, alias: CENTLAT, length: 11 )
        CENTLON ( type: esriFieldTypeString, alias: CENTLON, length: 12 )
        INTPTLAT ( type: esriFieldTypeString, alias: INTPTLAT, length: 11 )
        INTPTLON ( type: esriFieldTypeString, alias: INTPTLON, length: 12 )
        OBJECTID ( type: esriFieldTypeOID, alias: OBJECTID )

        returns the centroid of a zip area in lon, lat
        """
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
        """ 
        [Layer: 119th Congressional Districts (ID: 54)](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/54
        
        outFields: 
        MTFCC ( type: esriFieldTypeString, alias: MTFCC, length: 5 )
        OID ( type: esriFieldTypeString, alias: OID, length: 22 )
        GEOID ( type: esriFieldTypeString, alias: GEOID, length: 4 )
        STATE ( type: esriFieldTypeString, alias: STATE, length: 2 )
        BASENAME ( type: esriFieldTypeString, alias: BASENAME, length: 100 )
        NAME ( type: esriFieldTypeString, alias: NAME, length: 100 )
        LSADC ( type: esriFieldTypeString, alias: LSADC, length: 2 )
        FUNCSTAT ( type: esriFieldTypeString, alias: FUNCSTAT, length: 1 )
        AREALAND ( type: esriFieldTypeString, alias: AREALAND, length: 20 )
        AREAWATER ( type: esriFieldTypeString, alias: AREAWATER, length: 20 )
        CDSESSN ( type: esriFieldTypeString, alias: CDSESSN, length: 3 )
        OBJECTID ( type: esriFieldTypeOID, alias: OBJECTID )
        STGEOMETRY ( type: esriFieldTypeGeometry, alias: STGEOMETRY )
        CENTLAT ( type: esriFieldTypeString, alias: CENTLAT, length: 11 )
        CENTLON ( type: esriFieldTypeString, alias: CENTLON, length: 12 )
        INTPTLAT ( type: esriFieldTypeString, alias: INTPTLAT, length: 11 )
        INTPTLON ( type: esriFieldTypeString, alias: INTPTLON, length: 12 )
        CD119 ( type: esriFieldTypeString, alias: CD119, length: 2 )
        returns a list of features: which are the congressional districts in the area? 
        
        """
        params = {
            "geometry": f"{lon},{lat}",
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
