from app.api.api_services import institution


class businessServices:
    def userCreation(self, institute, name, email, password, verification='basic', pin=None):
        return institution.createUser(name=name, email=email, password=password, verificationType=verification,
                pin=pin, institute_id=institute)

    def institutionCreation(self, name, address, campuses):
        return institution.createNewInstitution(name=name, address=address, campus=campuses)

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


