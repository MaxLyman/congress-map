import src.utils.typesafe_utils as t

from typing import Dict
from src.classes.fetcher import Fetcher


class Congress:
    def __init__(self, fetcher: Fetcher):
        self.f: Fetcher = fetcher

    # NATIVE API FUNCTIONALITY
    def get_congress(self) -> Dict:
        """ 
            GET/congress Returns a list of congresses and congressional sessions.
        """
        response = self.f.get("congress")
        return response.content

    def get_congress_info(self, congress: int) -> Dict:
        """
            GET/congress/{congress} Returns detailed information for a specified congress.
        """
        response = self.f.get(f"congress/{congress}")
        return response.content

    def get_current_congress(self) -> Dict:
        """
            GET/congress/current Returns detailed information for the current congress.
        """
        response = self.f.get("congress/current")
        return response.content


    # CUSTOM 
    def get_current_congress_number(self) -> int:
        """returns current congress number -1 if error"""

        response = self.f.get("congress/current")

        if response.status_code == 200:
            return t.dig(response.content, ["congress", "number"],  -1)
    
        return -1 
        
        




if __name__ == "__main__":

    fetcher = Fetcher()
    congress_api_wrapper = Congress(fetcher)

    print(congress_api_wrapper.get_current_congress_number())
