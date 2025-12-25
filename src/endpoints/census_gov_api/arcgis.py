from pprint import pprint
import src.utils.typesafe_utils as t


from typing import Optional
from src.classes.fetcher import Fetcher

# its late ill do this later but basically i need something to make the address -> district code call
# and zip -> to district code call  etc. 



class Arcgis:

    def __init__(self, fetcher:Optional[Fetcher] ):
        #TODO: i kinda want to keep the fetcher profiles in the classes? 
        #      it would let me have more dynamic import structures
        self.f: Fetcher = fetcher
        
    def get_arcgis_address(self, address: str):

        response = self.f.get(
            # Use geographies/* to include geoLookup (e.g., congressional district)
            'geographies/onelineaddress',
            params={
                "address": address
            }    
        )

        return response.content





if __name__ == '__main__':
    from src.endpoints.census_gov_api.fetcher_profile import PROFILE


    fetcher = Fetcher(PROFILE)

    arcgis_api = Arcgis(fetcher)
    response = arcgis_api.get_arcgis_address("212 Boston ave, Somerville, MA")

    pprint(response)