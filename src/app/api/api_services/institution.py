from app.api.api_services.dependencies.unique_id import unique_id, provider_id
from typing import List, Union
from app.api.api_services.campus import campus
import app.api.api_services.users as usImport

class institution:
    def __init__(self, address:str, campuses:Union[List[campus], None], name:str):
        self.address = address
        self.campuses = campuses
        self.name = name
        self.id = str(unique_id(org_name=self.name.lower(), special_tag=""))
        self.users = []
        self.admins = []

    def setAdmin(self, user_id):
        self.admins.append(user_id)

    def setUser(self, user_id):
        self.users.append(user_id)

institutions = []
providers = []


def _find_campus(institute:institution, campus_id:str):
    if institute.campuses:
        try:
            c_index = [campus.campus_id for campus in institute.campuses].index(campus_id)
        except ValueError:
            c_index = -1
        return c_index

def _find_buildings(camp:campus, building_id:str):
    if camp.buildings:
        try:
            b_index = [build.building_id for build in camp.buildings].index(building_id)
        except ValueError:
            b_index = -1
        return b_index

def _find_room(build, room_id:str):
    if build.rooms:
        try:
            r_index = [room.room_id for room in build.rooms].index(room_id)
        except ValueError:
            r_index = -1
        return r_index


def getAddress(instituion):
    return instituion.address

def addCampus(institution, campus):
    institution.campuses.append(campus)

def getCampuses(institution):
    return institution.campuses

def getCampus(institution, campus_id):
    for campus in institution.campuses:
        if campus.campus_id == campus_id:
            return campus
    return None

def getName(institution):
    return institution.name

def createNewInstitution(name, address, campus):
    """
    Creates a new institution. An institution will be the representation of an
    organization/company/school etc.
    :param name: name of the institution
    :param address: address of the institution
    :param campus: a list of campuses associated with this institution
    :return: an dictionary object with the confirmed response information
    """
    if name and address and campus:
        newInstitute = institution(name=name, campuses=campus, address=address)
        institutions.append(newInstitute)
        return {"institution_name": name, "institution_address": address,
                "associated_campuses": campus, "institution_Id": newInstitute.id}
    return

def createNewCampus(name, address, buildings, institution_id):
    """
    Creates a new campus. A campus will be the representation of an
    organization/company/school etc.
    :param name: name of the campus
    :param address: address of the campus
    :param building: a list of buildings associated with this campus
    :return: an dictionary object with the confirmed response information
    """
    if name and address and buildings:
        newCampus = campus(name=name, buildings=buildings, address=address)
        institution = __findInstitute(institution_id)
        if institution != -1:
            institutions[institution].campuses.append(newCampus)
            return {"campus_name": name, "campus_address": address,
                    "associated_buildings": buildings, "campus_Id": newCampus.campus_id}
    return

def __findInstitute(institute_id):
    """
    Searches the institutes array for an institute.
    TODO: Change this to search for a specified ID
    :param institute_id: unique id of the institution
    :return: the index of the requested institute
    """
    try:
        index = [x.id for x in institutions].index(institute_id)
    except ValueError:
        index = -1
    return index


def getInstitute_from_Institutes(institute_id):
    """
    Handler function that will search for a specified institute.
    :param institute: desired institution
    :return: a dictionary of the JSON response
    """
    institute_index = __findInstitute(institute_id)
    if institute_index != -1:
        found = institutions[institute_index]
        return {"institution_name": found.name, "institution_address": found.address,
                "associated_campuses":found.campuses}


