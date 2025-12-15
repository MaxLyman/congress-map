from src.classes.fetcher import Fetcher


from src.endpoints.congress_gov_api.fetcher_profile import PROFILE as CONGRESS_PROFILE
from src.endpoints.congress_gov_api.congress import Congress
from src.endpoints.congress_gov_api.members import Member


from src.endpoints.census_gov_api.fetcher_profile import PROFILE as CENSUS_PROFILE
from src.endpoints.census_gov_api.arcgis import Arcgis

congress_fetcher = Fetcher(CONGRESS_PROFILE)

congress = Congress(congress_fetcher)
member = Member(congress_fetcher)


census_fetcher = Fetcher(CENSUS_PROFILE)
arcgis = Arcgis(census_fetcher)








# FLASK APP

#GET ~/congress/districts?zipcode={zipcode} -> {}

#GET ~/congress/representatives?address={address} -> {}



