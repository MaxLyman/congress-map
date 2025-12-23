from typing import Dict, List
from src.classes.fetcher import Fetcher


class Member():

    def __init__(self, fetcher: Fetcher):
        self.f:Fetcher = fetcher
    
    # NATIVE API FUNCTIONALITY
    def get_member(self) -> Dict:
        """
            get_memberReturns a list of congressional members.
        """
        response = self.f.get("member")
        return response.content

    def get_member_bioguideid(self, bioguideid: int) -> Dict:
        """ get_member_bioguideIdReturns detailed information for a specified congressional member """
        response = self.f.get(f"member/{bioguideid}")
        return response.content

    
    def get_member_bioguideid_sponsored_legislation(self, bioguideid: int) -> Dict:
        """
            get_member_bioguideId_sponsored_legislation 
            Returns the list of legislation sponsored by a specified congressional member.:
        """
        response = self.f.get(f"member/{bioguideid}/sponsored-legistlation")
        return response.content

    
    def get_member_bioguide_id_cosponsored_legislation(self, bioguideid: int) -> Dict:
        """
            get_member_bioguideId_cosponsored_legislationReturns the list of legislation 
            cosponsored by a specified congressional member.:
        """
        response = self.f.get(f"member/{bioguideid}/cosponsored-legistlation")
        return response.content

    
    def get_member_congress_(self, congress: int) -> Dict:
        """
            get_member_congress_ Returns the list of members specified by Congress:
        """
        response = self.f.get(f"member/congress/{congress}")
        return response.content

    def get_member_statecode(self, state_code: int) -> Dict:
        """
            get_member_stateCodeReturns a list of members filtered by state.:
        """
        response = self.f.get(f"member/{state_code}")
        return response.content

    
    def get_member_statecode_district(self, state_code:str, district: int) -> Dict:
        """
            get_member_stateCode_districtReturns a list of members filtered by state and district.:
        """
        response = self.f.get(f"member/{state_code}/{district}")
        return response.content

    def get_member_congress_statecode_district(self, congress:int, state_code:str, district:str) -> Dict:
        """
            get_member_congress_congress_stateCode_districtReturns a list of members filtered by congress, state and district.:
        """
        response = self.f.get(f"member/congress/{congress}/{state_code}/{district}")
        return response.content





if __name__ == "__main__":
    from src.utils.misc_utils import fips_to_abbr
    from src.endpoints.congress_gov_api.fetcher_profile import PROFILE as CONGRESS_PROFILE

    from src.endpoints.congress_gov_api.members import Member
    congress_fetcher = Fetcher(CONGRESS_PROFILE)

    member = Member(congress_fetcher)


    response = member.get_member_congress_statecode_district(119, fips_to_abbr('36'), '07')

    print(response)

