from app.api.api_services.dependencies.unique_id import unique_id, provider_id
from typing import List, Union
from app.api.api_services.campus import campus
from app.api.api_services.buildings import building, room
import app.api.api_services.users as us_import
import app.api.downstreamServices.database.Creation_Functions as cf

class institution:
    def __init__(self, campuses: Union[List, None], name:str, provider=None):
        """
        Institution class object.
            :param address: address of the institution
            :param campuses: list of campus information that will be created at the time of creation
            :param name: name of the institution
        """
        self.campuses = [campus(name=camp.campus_name, address=camp.campus_address, buildings=None) for camp
                         in campuses] if campuses != [None] else []
        self.name = name
        if ' ' in self.name:
            secondLetter = self.name.find(' ') + 1 if self.name.find(' ') != len(name) - 1 else 1
            self.orgTag = name[0] + self.name[secondLetter]
        else:
            self.orgTag = name[:2]

        self.id = str(unique_id(org_name=self.orgTag))
        self.users = []
        self.admins = []
        self.total_campuses = len(self.campuses)

        if self.campuses:
            self.__campusDefaultSets()

    def __campusDefaultSets(self):
        i = 1
        for campus in self.campuses:
            campus.setInstitution(self.id)
            campus.setCampus_id(i)
            i += 1

    def sendCampusesToDatabase(self):
        for campus in self.campuses:
            cf.create_campus(institution_id=self.id, campus_id=campus.campus_id, long=campus.lon, lat=campus.lat,
                             provider_id=campus.prov, name=campus.name, campus_address=campus.address)

    def addCampus(self, camp:campus):
        camp.setInstitution(self.id)
        self.total_campuses += 1
        camp.setCampus_id(self.total_campuses)
        self.campuses.append(camp)
    def setAdmin(self, user_id):
        if user_id not in self.admins:
            self.admins.append(user_id)
            if user_id in self.users:
                self.users.remove(user_id)


    def getCampusInfo(self, campus_id):
        pass


    def setUser(self, user_id):
        self.users.append(user_id)

providers = []
institutions = []

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

def getName(institution):
    return institution.name

def createNewInstitution(name, prov, campus):
    """
    Creates a new institution. An institution will be the representation of an
    organization/company/school etc.
    :param name: name of the institution
    :param address: address of the institution
    :param campus: a list of campuses associated with this institution
    :return: an dictionary object with the confirmed response information
    """
    if name and prov:

        newInstitute = institution(name=name, campuses=campus,provider=prov)
        cf.create_institution(institution_id=newInstitute.id, institution_name=name, provider_id=prov)
        newInstitute.sendCampusesToDatabase()
        campuses = [] if not campus else [{"campus_id": camp.campus_id, "campus_name": camp.name,
                                           "campus_address": camp.address} for camp in newInstitute.campuses]
        return {"institution_name": name, "provider": prov,
                "associated_campuses": campuses, "institution_Id": newInstitute.id}
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
    if name and address:
        newCampus = campus(name=name, buildings=buildings, address=address)
        newCampus.setInstitution(institution_id=institution_id)
        newCampus.setCampus_id()
        # institution = __findInstitute(institution_id)
        # if institution != -1:
            # institutions[institution].addCampus(newCampus)
        cf.create_campus(institution_id=institution_id, campus_id=newCampus.campus_id, long=newCampus.lon,
                             lat=newCampus.lat, name=newCampus.name, campus_address=newCampus.address)
        if newCampus.buildings:
            buildings = [{'building_id': bd.building_id, "building_name": bd.name} for bd in newCampus.buildings]
            for bd in newCampus.buildings:
                cf.create_building(campus_id, building_id, building_name, building_address, manager)

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

def __findCampus(institution, campus_id):
    for campus in institution.campuses:
        if campus.campus_id == campus_id:
            return campus
    return None



def getInstitute_from_Institutes(institute_id):
    """
    Handler function that will search for a specified institute.
    :param institute: desired institution
    :return: a dictionary of the JSON response
    """
    # institute_index = __findInstitute(institute_id)
    # if institute_index != -1:
      #  found = institutions[institute_index]
    try:
        found = dict(cf.getInst(institute_id)[0])
        return {"institution_name": found.get('institution_name'), "institution_id": found.get("institutionID")}
    except IndexError:
        return

def getCampus(institution_id, campus_id):
    institution = getInstitute_from_Institutes(institution_id)
    for campus in institution["associated_campuses"]:
        if campus.campus_id == campus_id:
            return {"campus_name": campus.name, "campus_address": campus.address,
                    "associated_buildings": campus.buildings, "campus_Id": campus.campus_id}
    return None

def getCampuses(institution_id):
    # institution = getInstitute_from_Institutes(institution_id)
    # campuses = []
    # for campus in institution["associated_campuses"]:
    #     temp = {"campus_name": campus.name, "campus_address": campus.address,
    #         "associated_buildings": campus.buildings, "campus_Id": campus.campus_id}
    #     campuses.append(temp)
    campuses = cf.getInstCamps(institution_id)
    return {"associated_campuses": campuses}

def getSpecificBuilding(institution_id, campus_id, building_id):
    # campus = getCampus(institution_id, campus_id)
    # for building in campus["associated_buildings"]:
    #     if building.building_id == building_id:
    #         return building
    building = cf.getCampBuilds(campus_id)
    return buildingInfo

def getBuildings(institution_id, campus_id):
    associated_buildings = cf.getCampBuilds(campus_id)
    return {"associated_buildings": associated_buildings}

def createUser(name:tuple, email, password, institute_id, verificationType='basic', pin=None):
    login = us_import.credentials(email=email, password=password)
    institution_index = __findInstitute(institute_id)
    if institution_index != -1:
        if pin:
            newUser = us_import.admin(name=name, login=login, institution_id=institute_id,
                                     verification_type=verificationType, pin=pin)
            newUser.setUserId()
            institutions[institution_index].admins.append(newUser.userId)
        else:
            newUser = us_import.user(name=name, login=login, institution_id=institute_id,
                                    verification_type=verificationType)
            newUser.setUserId()
            institutions[institution_index].users.append(newUser.userId)
        return {'user_id': newUser.userId, 'name': f"{newUser.first_name} {newUser.last_name}",
                'email': newUser.email, 'institution_id': institute_id, 'permissions': newUser.permissions,
                'validated': newUser.validated}
    return


def addNewBuilding(institution_id, campus_id, name, address, rooms, manager, consumption):
    # TODO: Integrate this with the database using the campus_id and the institution_id
    # institute_index = __findInstitute(institution_id)
    if name and address and manager and consumption:
        # campus = __findCampus(institution=institutions[institute_index], campus_id=campus_id)
        # if campus:
        roomsList = set()
        if rooms and rooms != [None]:
            for rm in rooms:
                rm_i = room(temp=rm.temp, room_number=rm.number, length=rm.length, width=rm.width, max_occupancy=rm.space,
                            height=rm.height)
                roomsList.update([rm_i])

        newBuilding = building(name=name, address=address, manager=manager, consumption=consumption, rooms=list(roomsList))
        newBuilding.setCampus(campus_id)
        newBuilding.setBuilding_id()
        newBuilding.assignRooms()
        cf.create_building(campus_id=campus_id, building_id=newBuilding.building_id, building_name=newBuilding.name,
                           building_address=newBuilding.address, manager=newBuilding.manager)
        for rm in roomsList:
            cf.create_room(building_id=newBuilding.building_id, room_num=rm.room_number, room_id=rm.room_id,
                           length=rm.length, width=rm.width, height=rm.height, volume=rm.max_occupancy,
                           temp=int(rm.desired_temp[:-1]))
        # newBuilding.assignRooms()
        # campus.addBuilding(newBuilding)
        nB_rooms = list() if not roomsList else [{"room_id": rm.room_id, "max_occupancy": rm.max_occupancy,
                                              "desired_temp": rm.desired_temp, "length": rm.length,
                                              "width": rm.width, "height": rm.height} for rm in roomsList]
        return {"building_id": newBuilding.building_id, "building_name": newBuilding.name, "manager": newBuilding.manager,
                "building_address": newBuilding.address, "average_energy_consumption": newBuilding.monthly_energy_consumption,
                "rooms_list": nB_rooms}
    return


def addNewRoom(institution_id, campus_id, building_id, rm):
    if rm:
        newRoom = room(temp=rm.temp, length=rm.length, width=rm.width, height=rm.height, max_occupancy=rm.space,
                       room_number=rm.number)
        newRoom.setBuilding_id(building_id)
        newRoom.setRoom_id()
        cf.create_room(building_id=building_id, room_num=newRoom.room_number, room_id=newRoom.room_id,
                           length=newRoom.length, width=newRoom.width, height=newRoom.height, volume=newRoom.max_occupancy,
                           temp=int(newRoom.desired_temp[:-1]))
        return {"room_id": newRoom.room_id, "room_number": newRoom.room_number, "length": newRoom.length,
                "width": newRoom.width, "height": newRoom.height, "desired_room_temp": newRoom.desired_temp,
                "max_occupancy": newRoom.max_occupancy}
    return

def get_allroom_information(institutionId, campusId, buildingId):
    all_rooms = cf.getBuildRooms(buildingId)
    return all_rooms



