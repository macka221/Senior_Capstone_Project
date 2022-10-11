from app.api.api_services.dependencies.unique_id import unique_id, provider_id

class institution:
    def __init__(self, address, campuses, name):
        self.address = address
        self.campuses = campuses
        self.name = name
        self.id = str(unique_id(org_name=self.name.lower(), special_tag=""))


class campus:
    def __init__(self, address, buildings, name):
        self.address = address
        self.buildings = buildings
        self.name = name

    def getAddress(self):
        return self.address

    def addBuilding(self, building):
        self.buildings.append(building)

    def getBuildings(self):
        return self.buildings

    def getName(self):
        return self.name

class building:
    def __init__(self, address, rooms, name, admin,provider, consumption):
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

    def getName(self):
        return self.name

class room:
    def __init__(self, name, temp, len, width, height, max_occupancy, prov):
        self.name = name
        self.desired_temp = temp
        self.len = len
        self.width = width
        self.height = height
        self.max_occupancy = max_occupancy
        self.provider = prov

    def getName(self):
        return self.name

    def getDesiredtemp(self):
        return self.desired_temp

    def setDesiredtemp(self, temp):
        self.desired_temp = temp

    def getMaxOccupancy(self):
        return self.max_occupancy

class provider:
    def __init__(self, name, rate, cost):
        self.rate = rate
        self.name = provider
        self.monthly_cost = cost

    def setMonthlyCost(self, cost):
        self.monthly_costcost = cost

    def getMonthlyCost(self):
        return self.monthly_cost


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


