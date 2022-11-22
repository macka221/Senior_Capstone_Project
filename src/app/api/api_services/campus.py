from app.api.api_services.buildings import building
from typing import Union, List

class provider:
    def __init__(self, name:str, rate:float, cost:float):
        self.rate = rate
        self.name = provider
        self.monthly_cost = cost

    def setMonthlyCost(self, cost):
        self.monthly_costcost = cost

    def getMonthlyCost(self):
        return self.monthly_cost


class campus:
    def __init__(self, address:str, buildings:Union[List[building], None],name:str, long:float, lat:float):
        # TODO: incorporate provider into this class
        self.address = address
        self.buildings = buildings if buildings else []
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
        self.campus_id = self.institution + f"-C-{''.join(self.name.split()).lower()[:5]}-{campus_number}"

    def assignBuildings(self):
        for item in self.buildings:
            item.setCampus(self.campus_id)

    def getLong(self):
        return self.long

    def getLat(self):
        return self.lat

def getBuildings(campus):
    return campus.buildings

def getBuilding(campus, building_id):
    for building in campus.buildings:
        if building.building_id == building_id:
            return building
    return