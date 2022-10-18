from pydantic import constr
from app.api.api_services.dependencies.unique_id import unique_id


# ===============================================================
# Example Request Bodies
# ===============================================================

_NEW_INSTITUTION = {
        "summary": "A successful post for a new institution",
        "description": """A successful post should contain the institution name, address and associated campuses. Each field explained:\n
        - institution_name: the name of the organization or institution\n
        - institution_address: the main address for the institution\n
        - associated_campuses: a list of the associated campuses\n
        """,
        "value": {
            "institution_name": "Morehouse College",
            "institution_address": "830 Westview Dr SW Atlanta, GA, 30354",
            "associated_campuses": [
                "Morehouse College"
            ]
        }
    }

_NEW_CAMPUS = {
        "summary": "A successful post for a new campus",
        "description": """A successful post should contain the institution name, address and associated campuses. Each field explained:\n
        - campus_name: the name of the campus\n
        - campus_address: the main address for the campus\n
        - associated_buildings: a list of the associated buildings\n
        """,
        "value": {
            "campus_name": "Morehouse College",
            "campus_address": "830 Westview Dr SW Atlanta, GA, 30354",
            "associated_buildings": [
                "Morehouse College"
            ]
        }
    }
