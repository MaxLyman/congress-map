import src.utils.typesafe_utils as t
from src.utils.db_utils import create_app, Services

from flask import request, jsonify

app = create_app()

@app.route("/congress/districts", methods=["GET"])
def congress_districts():
    """GET ~/congress/districts?zipcode={zipcode} -> {}"""
    zipcode = t.dig(request.args, ["zipcode"])
    services: Services = app.extensions["services"]
    
    district_list = []
    if zipcode:
        district_list = services.census_service.district_from_zip_code(zipcode)

    if district_list:
        return jsonify({"content": district_list}, 200)

    return jsonify({"error_msg": "no zipcode or address found"}, 404)


@app.route("/congress/representatives", methods=["GET"])
def congress_representatives():
    """GET ~/congress/representatives?address={address} -> {}"""

    address = t.dig(request.args, ["address"])
    zipcode = t.dig(request.args, ["zipcode"])
    services: Services = app.extensions["services"]
    
    if not address and not zipcode:
        return  jsonify({"error_msg": "no zipcode or address found"}, 404)

    if address:
        district_list = services.census_service.district_from_address(address)

    if zipcode:
        district_list = services.census_service.district_from_zip_code(zipcode)
        

    congressional_reps = services.congress_service.congressional_members_in_district(district_list)

    if not congressional_reps:
        jsonify({"content": congressional_reps}, 404)

    return jsonify({"content": congressional_reps}, 200)
    




if __name__ == "__main__":
    # Dev server entrypoint (prefer `flask --app congress_map_service:app run` for reload/debug)
    # app.run(host="127.0.0.1", port=5000, debug=True)
    # /congress/representatives", query_string={"address": "212 Boston ave, Somerville, MA"})


    from pprint import pprint

    app.testing = True
    with app.test_client() as c:
        r = c.get(
            "/congress/representatives",
            query_string={"address": "122 Boston ave, Somerville, MA"},
        )
        print(r.status_code)
        pprint(r.get_json())