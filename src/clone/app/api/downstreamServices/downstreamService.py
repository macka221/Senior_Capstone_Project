from app.api.api_services import institution


class businessServices(object):
    def userCreation(institution, name, email, manager):
        return True

    def institutionCreation(name, address, campuses):
        return True

    def buildingCreation(instituteId, name, address, rooms, manager, provider, consumption, cost):
        return True


