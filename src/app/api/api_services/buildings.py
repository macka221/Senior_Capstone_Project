from typing import List, Union


class room:
    def __init__(self, temp:str, room_number, length:int, width:int, height:int, max_occupancy:int):
        self.desired_temp = temp
        self.length = length
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
    
    def setBuilding_id(self, building_id):
        self.building = building_id

    def setRoom_id(self):
        self.room_id = self.building + f"-R-{self.room_number}"


class building:
    def __init__(self, address:str, rooms:Union[List[room], None], name:str, manager:str, consumption:float):
        self.address = address
        self.name = name
        self.manager = manager
        self.rooms = rooms
        self.monthly_energy_consumption = consumption
        self.campus_id = None
        self.building_id = None

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
        self.building_id = self.campus_id + f"-B-{self.name.lower()[:3]}"
    
    def assignRooms(self):
        for item in self.rooms:
            item.setBuilding_id(self.building_id)
            item.setRoom_id()



