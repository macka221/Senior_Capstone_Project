from typing import List, Union
from app.api.api_services.users import admin, superuser

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
    def __init__(self, name:str, temp:str, length:int, width:int, height:int, max_occupancy:int):
        self.name = name
        self.desired_temp = temp
        self.len = length
        self.width = width
        self.height = height
        self.max_occupancy = max_occupancy

    def getName(self):
        return self.name

    def getDesiredtemp(self):
        return self.desired_temp

    def setDesiredtemp(self, temp):
        self.desired_temp = temp

    def getMaxOccupancy(self):
        return self.max_occupancy



class building:
    def __init__(self, address:str, rooms:Union[List[room], None], name:str, admin:Union[admin, superuser], provider:provider, consumption:float):
        self.address = address
        self.name = name
        self.admin = admin
        self.rooms = rooms
        self.energy_provider = provider
        self.monthly_energy_consumption = consumption

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


