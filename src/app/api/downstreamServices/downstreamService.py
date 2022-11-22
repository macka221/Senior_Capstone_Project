from app.api.api_services import institution
from app.api.api_services import campus
from app.api.api_services import energy


class businessServices:
    def userCreation(self, institute, name, email, password, verification='basic', pin=None):
        return institution.createUser(name=name, email=email, password=password, verificationType=verification,
                pin=pin, institute_id=institute)

    def institutionCreation(self, name, prov, campuses):
        return institution.createNewInstitution(name=name, campus=campuses, prov=prov)

    def campusCreation(self, name, address, buildings, institution_id):
        return institution.createNewCampus(name=name, address=address, buildings=buildings,
                                                institution_id=institution_id)

    def buildingCreation(self, instituteId, name, address, manager, consumption, campus_id, rooms):
        return institution.addNewBuilding(institution_id=instituteId, name=name, address=address, rooms=rooms,
                                          consumption=consumption, manager=manager, campus_id=campus_id)

    def getInstitution(self, institute_id):
        return institution.getInstitute_from_Institutes(institute_id=institute_id)

    def getCampus(self, institution_id, campus_id):
        return institution.getCampus(institution_id=institution_id, campus_id=campus_id)

    def getCampuses(self, institution_id):
        return institution.getCampuses(institution_id=institution_id)

    def getBuilding(self, institution_id, campus_id, building_id):
        return institution.getBuilding(institution_id=institution_id, campus_id=campus_id, building_id=building_id)

    def getBuildings(self, institution_id, campus_id):
        return institution.getBuildings(institution_id=institution_id, campus_id=campus_id)

    def createNewRoom(self, institution_id, campus_id, building_id, room):
        return institution.addNewRoom(institution_id=institution_id, campus_id=campus_id, building_id=building_id,
                                      rm=room)
    def calculateEnergyCostBuildingPerDay(self, institution_id, campus_id, building_id):
        long = institution.getLongitude(institution_id=institution_id, campus_id=campus_id)
        lat = institution.getLatitude(institution_id=institution_id, campus_id=campus_id)
        building = institution.getBuilding(institution_id, campus_id, building_id)
        return energy.calculateEnergyCostBuildingPerDay(building, long, lat)

    def calculateEnergyCostBuildingWeekForcast(self, institution_id, campus_id, building_id):
        long = institution.getLongitude(institution_id=institution_id, campus_id=campus_id)
        lat = institution.getLatitude(institution_id=institution_id, campus_id=campus_id)
        building = institution.getBuilding(institution_id, campus_id, building_id)
        return energy.calculateEnergyCostBuildingPer(building, long, lat)

    def get_all_rooms(self, institution_id, campus_id, building_id):
        return institution.get_allroom_information(institution_id, campus_id, building_id)

