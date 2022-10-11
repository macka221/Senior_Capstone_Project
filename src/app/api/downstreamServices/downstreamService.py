from app.api.api_services import institution


class businessServices:
    def userCreation(self, institution, name, email, manager):
        return True

    def institutionCreation(self, name, address, campuses):
        return institution.createNewInstitution(name=name, address=address, campus=campuses)

    def buildingCreation(self, instituteId, name, address, rooms, manager, provider, consumption, cost):
        return True

    def getInstitution(self, institute_id):
        return institution.getInstitute_from_Institutes(institute_id=institute_id)


