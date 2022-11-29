from app.api.api_services.buildings import building
from typing import Union, List
import requests
import urllib.parse
import uuid

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
    def __init__(self, address:str, buildings:Union[List[building], None],name:str):
        # TODO: incorporate provider into this class
        self.address = address
        self.buildings = buildings if buildings else []
        self.name = name
        self.institution = None
        self.campus_id = None
        self.buildingNumber = len(buildings) if buildings else 0
        self.prov = "Deprecated"
        
        self.__setLonLat()
        if buildings:
            self.createBuildings()

    
    def createBuildings(self):
        self.buildings = []
        for build in self.buildings:
            newBuilding = building(address=build.address, rooms=None, name=build.name, manager=build.manager,
                    consumption=build.consumption)
            self.buildings.append(newBuilding)

    def __setLonLat(self):
        try:
            q_address = urllib.parse.quote(self.address)
            resp = requests.get(f'https://nominatim.openstreetmap.org/search/{q_address}?format=json')
            self.lat, self.lon = float(resp.json()[0]['lat']), float(resp.json()[0]['lon'])
        except IndexError as err:
            print(f"""Failed to locate the address against nominatim open street map API! Recieved the following error
            {err}
            
            Address should be in the following format
                <street_number> <street_name> <city_name>, <state>, <zipcode>
            An example of this is 830 Westview Dr SW Atlanta, GA, 30354. Please adjust accordingling and try again""")
            
            raise ValueError

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

    def setCampus_id(self):
        self.campus_id = self.institution + f"-C-{''.join(self.name.split()).lower()[:5]}-{str(uuid.uuid4())[:4]}"

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
