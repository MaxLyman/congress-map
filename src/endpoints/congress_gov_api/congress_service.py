import src.utils.typesafe_utils as t

from typing import List
from src.classes.fetcher import Fetcher

from src.endpoints.congress_gov_api.fetcher_profile import PROFILE
from src.endpoints.congress_gov_api.congress import Congress
from src.endpoints.congress_gov_api.members import Member

from src.endpoints.data_classes import District, CongressMember

class CongressService:
    fetcher_profile = Fetcher(PROFILE)

    member: Member      = Member(fetcher_profile)
    congress: Congress  = Congress(fetcher_profile)



    def congressional_members_in_district(self, district_list: List[District]) -> List[CongressMember]:
        congressional_reps = []
        if not isinstance(district, list):
            district_list = [district]

        if not district:
            return []
        
        congress_class = self.congress.get_current_congress_number()


        for district in district_list:
            congressional_reps.append(
                self.member.get_member_congress_statecode_district(
                    congress_class,
                    district.state_code,
                    district.district_code,
                )
            )

        return congressional_reps