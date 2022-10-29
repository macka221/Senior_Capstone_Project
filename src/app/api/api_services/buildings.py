from typing import List, Union


class provider:
    def __init__(self, name:str, rate:float, cost:float):
        self.rate = rate
        self.name = provider
        self.monthly_cost = cost

    def setMonthlyCost(self, cost):
        self.monthly_costcost = cost

    def getMonthlyCost(self):
        return self.monthly_cost


class room:
    def __init__(self, temp:str, room_number, length:int, width:int, height:int, max_occupancy:int):
        self.desired_temp = temp
        self.len = length
        self.width = width
        self.height = height
        self.max_occupancy = max_occupancy
        self.room_id = None
        self.building = None
        self.room_number = room_number

    def getRoom_Number(self):
        return self.room_number

    def getDesiredtemp(self):
        return self.desired_temp

    def setDesiredtemp(self, temp):
        self.desired_temp = temp

    def getMaxOccupancy(self):
        return self.max_occupancy
    
    def setBuilding(self, building_id):
        self.building = building_id

    def setRoom_id(self):
        self.room_id = self.building + f"-r-{self.room_number}"


class building:
    def __init__(self, address:str, rooms:Union[List[room], None], name:str, manager:str, provider:provider, consumption:float):
        self.address = address
        self.name = name
        self.manager = manager
        self.rooms = rooms
        self.energy_provider = provider
        self.monthly_energy_consumption = consumption
        self.campus_id = None
        self.building_id = None

    def setEnergyRateCost(self, rate):
        self.energy_rate_cost = rate

    def getEnergyRateCost(self):
        return self.energy_rate_cost

    def getEnergyProvider(self):
        return self.energy_provider

    def getAddress(self):
        return self.address

    def setMonthly_energy_consumption(self, energy):
        self.monthly_energy_consumption = energy

    def getMonthly_energy_consumption(self):
        return self.monthly_energy_consumption

    def addRooms(self, room):
        self.rooms.append(room)

    def getRooms(self):
        return self.rooms

    def setCampus(self, campus_id):
        self.campus_id = campus_id
    
    def setBuilding_id(self):
        self.building_id = self.campus_id + f"-b-{name.lower()}"
    
    def assignRooms(self):
        for item in self.rooms:
            item.setBuilding_id(self.building_id)



