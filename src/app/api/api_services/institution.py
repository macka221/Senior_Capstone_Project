from app.api.api_services.dependencies.unique_id import unique_id, provider_id
from typing import List, Union
from app.api.api_services.campus import campus

class institution:
    def __init__(self, address:str, campuses:Union[List[campus], None], name:str):
        self.address = address
        self.campuses = campuses
        self.name = name
        self.id = str(unique_id(org_name=self.name.lower(), special_tag=""))

institutions = []
providers = []

def getAddress(instituion):
    return instituion.address

def addCampus(institution):
    institution.campuses.append(campus)

def getCampuses(institution):
    return institution.campuses

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


