from app.api.api_services import institution


class businessServices:
    def userCreation(self, institute, name, email, password, verification='basic', pin=None):
        return institution.createUser(name=name, email=email, password=password, verificationType=verification,
                pin=pin, institute_id=institute)

    def institutionCreation(self, name, address, campuses):
        return institution.createNewInstitution(name=name, address=address, campus=campuses)

    def buildingCreation(self, instituteId, name, address, rooms, manager, provider, consumption, cost):
        return True

    def getInstitution(self, institute_id):
        return institution.getInstitute_from_Institutes(institute_id=institute_id)


