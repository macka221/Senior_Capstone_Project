from fastapi import FastAPI, HTTPException, Body
from starlette.responses import Response
from pydantic import BaseModel
from app.api.downstreamServices.downstreamService import businessServices
from typing import List
import app.api.routes.constants as c

app = FastAPI()

apiServices = businessServices()

class newUser(BaseModel):
    name: str = Body(default=..., alias="user_name")
    email: str = Body(default=..., alias="user_email")
    manager: bool = Body(default=False, alias="building_manager")

class newInstitution(BaseModel):
    name: str = Body(default=..., alias="institution_name")
    address: str = Body(default=..., alias="institution_address")
    campuses: List = Body(exclude_unset=True, alias="associated_campuses")

class newCampus(BaseModel):
    name: str = Body(default=..., alias="campus_name")
    address: str = Body(default=..., alias="campus_address")
    buildings: List = Body(exclude_unset=True, alias="associated_buildings")

class provider(BaseModel):
    name: str = Body(default=..., alias="provider_name")
    rate: float = Body(default=...)

class newBuilding(BaseModel):
    name:str = Body(default=..., alias="building_name")
    address: str = Body(default=..., alias="building_address")
    rooms: List[str] = Body(exclude_unset=True)
    prov: provider = Body(default=..., alias="provider")
    cost: float = Body(default=..., alias="cost_for_month")
    consumption: float = Body(default=..., alias="total_energy_consumption")
    manager: str = Body(default=..., alias="building_manager_id")

class Room(BaseModel):
    length: int = Body(alias="room_length", default=...)
    width: int = Body(alias="room_width", default=...)
    height: int = Body(alias="room_height", default=...)
    space: int = Body(alias="max_occupency", default=...)
    temp: str = Body(alias="desired_room_temp", default=...)


@app.post("/app/institutions", summary="Create a new Institution")
async def newInstitution(institutionInfo: newInstitution=Body(examples={"Successful Post": c._NEW_INSTITUTION})):
    """
    Use this endpoint if you would like to create a new instance of an institution. This requires a JSON body in the format of the example below.\n
    **param** institutionInfo: the JSON body with the required information to create a new institution\n
    **return**: the newly created object with it's unique id.\n
    **Ex)**\n

        {
            "institution_name": "<name_of_organization>",
            "institution_address": "<address_of_org>",
            "associated_campuses": [
                "<list_of_associated_campuses>"
            ]
        }
    """
    newInstitute = apiServices.institutionCreation(institutionInfo.name, institutionInfo.address, institutionInfo.campuses)
    if not newInstitute:
        raise HTTPException(status_code=404, detail="Failed to create institution!")
    return newInstitute


@app.get("/app/institutions/{institution_id}")
async def getInstitute(institution_id:str):
    institute = apiServices.getInstitution(institute_id=institution_id)
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    return institute


@app.post("/app/institutions/{institutionId}/buildings")
async def newBuilding(institutionId:str, buildingInfo: newBuilding):
    building = businessServices.buildingCreation(instituteId=institutionId, name=buildingInfo.name, address=buildingInfo.address,
                                         rooms=buildingInfo.rooms, provider=buildingInfo.prov, cost=buildingInfo.cost,
                                         consumption=buildingInfo.consumption, manager=buildingInfo.manager)
    if not building:
        raise HTTPException(status_code=404, detail="Failed to create the building!")
    return {"message": "Building Successfully Created"}


@app.post("/app/institutions/{institutionId}/users", summary="Creates a new user")
async def createNewUser(userInfo: newUser, institutionId: str):
    newUser = businessServices.userCreation(institution=institutionId, name=userInfo.name, email=userInfo.email,
                                    manager=userInfo.manager)
    if not newUser:
        raise HTTPException(status_code=404, detail="Failed to create user!")
    return {"message": "User created Successfully"}


@app.post("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}/rooms", summary="Creates a new room")
async def addRoomInformation(institution_id, campus_id, building_id, room:Room):
    pass


@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}/rooms", summary="Get all rooms associated with a buidling")
async def getAllRoomsInformation(institution_id:str, campus_id:str, building_id:str):
    pass


@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}/rooms/{room_id}", summary="Get specific room information")
async def getRoomInfo(institution_id:str, campus_id:str, building_id:str, room_id:str):
    pass


@app.get("/institutions/{institution_id}/users", summary="Get all user information")
async def getAllUsers(institution_id:str):
    pass


@app.get("/institutions/{institution_id}/users/{user_id}", summary="Get user information")
async def getUserInfo(institution_id:str, user_id:str):
    pass

@app.post("/institutions/{institution_id}/campuses", summary="Creates a new campus")
async def createNewCampus(campusInfo: newCampus=Body(examples={"Successful Post": c._NEW_CAMPUS})):
    newCampus = apiServices.campusCreation(campusInfo.name, campusInfo.address,
                                                   campusInfo.buildings)
    if not newCampus:
        raise HTTPException(status_code=404, detail="Failed to create campus!")
    return newCampus

@app.get("/institutions/{institution_id}/campuses/{campus_id}", summary="Gets a single campus information")
async def getCampus(institution_id:str, campus_id:str):
    institution = apiServices.getInstitution(institution_id=institution_id)
    campus = apiServices.getCampus(institute=institution, campus_id=campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    return campus

@app.get("/institutions/{institution_id}/campuses", summary="gets all campuses associated with an institution")
async def getAllCampuses(institution_id:str):
    institution = apiServices.getInstitution(institution_id=institution_id)
    if not institution:
        raise HTTPException(status_code=404, detail="Institution not found")
    campuses = apiServices.getCampuses(instituttion=institution)
    if not campuses:
        raise HTTPException(status_code=404, detail="No campuses found")
    return campuses

@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings", summary="gets all buildings associated with a campus")
async def geAllBuildings(institution_id:str, campus_id:str):
    institution = apiServices.getInstitution(institution_id=institution_id)
    if not institution:
        raise HTTPException(status_code=404, detail="Institution not found")
    campus = apiServices.getCampus(institute=institution, campus_id=campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    buildings = apiServices.getBuildings(campus=campus)
    if not buildings:
        raise HTTPException(status_code=404, detail="No buildings found")
    return buildings

@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}", summary="gets a specific buildings information")
async def getBuilding(institution_id:str, campus_id:str, building_id):
    institution = apiServices.getInstitution(institution_id=institution_id)
    if not institution:
        raise HTTPException(status_code=404, detail="Institution not found")
    campus = apiServices.getCampus(institute=institution, campus_id=campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    building = apiServices.building(campus=campus, building_id=building_id)
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    return building