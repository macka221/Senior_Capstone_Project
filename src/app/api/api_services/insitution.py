class institution:
    def __init__(self, address, campuses, name):
        self.address = address
        self.campuses = campuses
        self.name = name

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def addCampus(self, campus):
        self.campuses.append(campus)

    def getCampuses(self):
        return self.campuses

    def getName(self):
        return self.name

class campus:
    def __init__(self, address, buildings, name):
        self.address = address
        self.buildings = buildings
        self.name = name

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def addBuilding(self, building):
        self.buildings.append(building)

    def getBuildings(self):
        return self.buildings

    def getName(self):
        return self.name

class building:
    def __init__(self, address, rooms, name, admin, rate, provider, cost, consumption):
        self.address = address
        self.name = name
        self.admin = admin
        self.rooms = rooms
        self.energy_rate_cost = rate
        self.energy_provider = provider
        self.monthly_cost = cost
        self.monthly_energy_consumption = consumption

    def setEnergyRateCost(self, rate):
        self.energy_rate_cost = rate

    def getEnergyRateCost(self):
        return self.energy_rate_cost

    def getEnergyProvider(self):
        return self.energy_provider

    def setMonthlyCost(self, cost):
        self.monthly_cost = cost

    def setMonthlyConsumption(self, consumption):
        self.monthly_energy_consumption = consumption

    def getMonthlyCost(self):
        return self.monthly_cost

    def getMonthlyConsumption(self):
        return self.monthly_energy_consumption
    def setAddress(self, address):
        self.address = address

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

    def getName(self):
        return self.name

class room:
    def __init__(self, name, temp, len, width, height, max_occupancy):
        self.name = name
        self.desired_temp = temp
        self.len = len
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