from typing import List, Optional, Literal
from dataclasses import dataclass, asdict


Year = int
@dataclass
class CongressMember:
    name:               str
    state:              str
    party:              str
    profile_img:        str
    bioguide_id:        str
    fec_candidate_id:   str | None = None

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class Term: 
    chamber:        Literal["house", "senate"]
    member_id:      str
    start_year:     Year
    end_year:       Year | None = None


@dataclass
class District:
    district_code: str
    state_code: str


    


