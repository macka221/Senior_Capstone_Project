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
                {
                    "campus_name": "Morehouse College Main Campus",
                    "campus_address": "830 Westview Dr SW Atlanta, GA, 30354"
                }
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
            "campus_name": "Morehouse College Main Campus",
            "campus_address": "830 Westview Dr SW Atlanta, GA, 30354",
            "associated_buildings": [
                {
                    "building_name": "Dansby Hall",
                    "building_address": "830 Westview Dr SW 1 Atlanta, GA, 30354",
                    "total_energy_consumption": 1214.12,
                    "building_manager": "O-MC-0f29be-u-653b24"
                }
            ]
        }
    }

_NEW_BUILDINGS = {
    "summary" : "A successful post for new building",
    "description": """
    Required Values:\n
        - building_name: name of the building\n
        - building_address: address of the building\n
        - total_energy_consumption: total energy consumption for one year\n
        - building_manager_id: existing associated building manager's id\n
    
    Optional Values:\n
        - rooms: list of the room information\n
            - room_length: room's length in feet as an integer (ex. 5ft is just 5)\n
            - room_width: room's width in feet as an integer (ex. 5ft is just 5)\n
            - room_height: room's height in feet as an integer (ex. 5ft is just 5)\n
            - max_occupancy: room's maximum occupancy as an integer\n 
            - desired_room_temp: the desired room temperature in Celsius (ex. 40C)\n
            - room_number: the rooms number as an integer (ex. room 215 is just 215)\n
    """,
    "value": {
        "building_name": "Dansby Hall",
        "building_address": "830 Westview Dr SW 450, Atlanta, GA, 30345",
        "total_energy_consumption": 45000.00,
        "building_manager_id": "O-MC-0f29be-u-653b24",
        "rooms": [
            {
                "room_length": 5,
                "room_width": 5,
                "room_height": 5,
                "max_occupancy": 5,
                "desired_room_temp": "72C",
                "room_number": 201
            }
        ]
    }
}

_NEW_ROOM = {
    "summary": "Successful post of new room",
    "description": """
    All of the information below is required. Here is a description of each field.\n
        - room_length: room's length in feet as an integer (ex. 5ft is just 5)\n
        - room_width: room's width in feet as an integer (ex. 5ft is just 5)\n
        - room_height: room's height in feet as an integer (ex. 5ft is just 5)\n
        - max_occupancy: room's maximum occupancy as an integer\n 
        - desired_room_temp: the desired room temperature in Celsius (ex. 40C)\n
        - room_number: the rooms number as an integer (ex. room 215 is just 215)\n
    """,
    "value": {
        "room_length": 10,
        "room_width": 18,
        "room_height": 10,
        "max_occupancy": 12,
        "desired_room_temp": "72C",
        "room_number": 312
    }
}
