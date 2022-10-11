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
