import src.utils.typesafe_utils as t

from typing import List

from src.utils.misc_utils import get_current_congress, fips_to_abbr
from src.classes.fetcher import Fetcher
from src.endpoints.data_classes import District, CongressMember

from src.endpoints.census_gov_api.fetcher_profile import PROFILE
from src.endpoints.census_gov_api.arcgis import Arcgis
from src.endpoints.census_gov_api.tigerweb import Tigerweb


class CensusService:
    fetcher_profile     = Fetcher(PROFILE)
    arcgis: Arcgis      = Arcgis(fetcher_profile)
    tigerweb: Tigerweb  = Tigerweb(fetcher_profile)


    def district_from_zip_code(self, zipcode: str) -> List[District] | List[None]:

        if not zipcode:
            return []
        
        lon_lat = self.tigerweb.get_tigerweb_zip_to_centroid(zipcode)
        district_info = self.tigerweb.get_congressional_district_from_centroid(*lon_lat)


        if not isinstance(district_info, dict):
            return []
    
        districts_in_centroid = t.dig(district_info, ["features"], [])
        current_congress = get_current_congress()
        congress_code = f'CD{current_congress}'
        
        district_list = []
        for district in districts_in_centroid:
            district_list.append(
                District(
                    state_code=t.dig(district, ['attributes', 'STATE']),
                    district_code=t.dig(district, ['attributes', congress_code])
                )
            )
        return district_list



    def district_from_address(self, address: str) -> List[District] | List[None]:

        if not address:
            return []
        
        response_content = self.arcgis.get_arcgis_address(address)
        
        if not isinstance(response_content, dict):
            # TODO: add some logging
            return []
        
        geographies = t.dig(response_content, ["result", "addressMatches", 0, "geographies"], {})

        district_list = []
        for district in geographies.values():
            district = t.dig(district, [0], {})
            district

            district_list.append(
                District(
                    district_code=t.dig(district, ['BASENAME']),
                    state_code=fips_to_abbr(t.dig(district, ["STATE"]))

                )
            )
        return district_list
        
    




if __name__ == "__main__":
    cs = CensusService()
    cs.district_from_address("122 Boston ave, Somerville, MA")

        



        


        