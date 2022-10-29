from app.api.api_services.buildings import building
from typing import Union, List

class campus:
    def __init__(self, address:str, buildings:Union[List[building], None], name:str):
        self.address = address
        self.buildings = buildings
        self.name = name
        self.institution = None
        self.campus_id = None
        self.buildingNumber = len(buildings) if buildings else 0

    def getAddress(self):
        return self.address

    def addBuilding(self, building):
        self.buildings.append(building)
        self.buildingNumber += 1

    def getBuildings(self):
        return self.buildings

    def getName(self):
        return self.name
    
    def setInstitution(self, institution_id):
        self.institution = institution_id

    def setCampus_id(self, campus_number:int):
        self.campus_id = self.institution + f"-n-{self.name.lower()}-{campus_number}"

    def assignBuildings(self):
        for item in self.buildings:
            item.setCampus(self.campus_id)

def getBuildings(campus):
    return campus.buildings

def getBuilding(campus, building_id):
    for building in campus.buildings:
        if building.building_id == building_id:
            return building
    return None