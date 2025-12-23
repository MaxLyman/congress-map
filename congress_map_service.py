import src.utils.typesafe_utils as t
from src.utils.misc_utils import fips_to_abbr
from flask import Flask, request, jsonify

from src.classes.fetcher import Fetcher
from src.endpoints.congress_gov_api.fetcher_profile import PROFILE as CONGRESS_PROFILE
from src.endpoints.congress_gov_api.congress import Congress
from src.endpoints.congress_gov_api.members import Member

from src.endpoints.census_gov_api.fetcher_profile import PROFILE as CENSUS_PROFILE
from src.endpoints.census_gov_api.arcgis import Arcgis
from src.endpoints.census_gov_api.tigerweb import Tigerweb



app = Flask(__name__)
congress_fetcher = Fetcher(CONGRESS_PROFILE)

congress = Congress(congress_fetcher)
member = Member(congress_fetcher)


census_fetcher = Fetcher(CENSUS_PROFILE)
arcgis = Arcgis(census_fetcher)

tiger_fetcher = Tigerweb()


CURRENT_CONGRESS = congress.get_current_congress_number()

@app.route("/congress/districts", methods=["GET"])
def congress_districts():
    """GET ~/congress/districts?zipcode={zipcode} -> {}"""
    zipcode = t.dig(request.args, ["zipcode"])

    if zipcode:

        return jsonify("ZIPCODE DISTRICTS")


    return jsonify({"error_msg": "no zipcode or address found"}, 404)


@app.route("/congress/representatives", methods=["GET"])
def congress_representatives():
    """GET ~/congress/representatives?address={address} -> {}"""

    address = t.dig(request.args, ["address"])
    zipcode = t.dig(request.args, ["zipcode"])

    congressional_reps = []

    if address:
        return jsonify("ADDRESS RESPONSE")
    

    if zipcode:

        lon_lat = tiger_fetcher.get_tigerweb_zip_to_centroid(zipcode)
        district_info = tiger_fetcher.get_congressional_district_from_centroid(*lon_lat)

        districts_in_centroid = t.dig(district_info, ["features"], [])
        for district_attr in districts_in_centroid:
            state_code = fips_to_abbr(t.dig(district_attr, ['attributes', 'STATE']))
            congress_code = f'CD{CURRENT_CONGRESS}'

            district = t.dig(district_attr, ['attributes', congress_code])

            congressional_reps.append(
                member.get_member_congress_statecode_district(
                    CURRENT_CONGRESS,
                    state_code,
                    district
                )
            )

        return jsonify({"content": congressional_reps}, 200)


    return  jsonify({"error_msg": "no zipcode or address found"}, 404)




if __name__ == "__main__":
    app.testing = True
    with app.test_client() as c:
        r = c.get("/congress/representatives", query_string={"zipcode": "11211"})
        print(r.status_code)
        print(r.get_json())