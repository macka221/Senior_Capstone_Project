from fastapi import FastAPI, HTTPException, Body
from starlette.responses import Response
from pydantic import BaseModel
from app.api.downstreamServices.downstreamService import businessServices
from typing import List, Union
import app.api.routes.constants as c
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
# TODO: Change the allow_origins to specify a url
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"]
        )
apiServices = businessServices()


class newUser(BaseModel):
    first_name: str = Body(default=...)
    last_name: str = Body(default=...)
    email: str = Body(default=..., alias="user_email")
    password: str = Body(default=..., alias="user_password")
    verification_type:str = Body(default='basic')
    pin:Union[int, None] = Body(default=None, exclude_unset=True)

class campusInfoBasic(BaseModel):
    campus_name: str = Body(default=...)
    campus_address: str = Body(default=...)


class provider(BaseModel):
    name: str = Body(default=..., alias="provider_name")
    rate: float = Body(default=...)

class newInstitution(BaseModel):
    name: str = Body(default=..., alias="institution_name")
    address: str = Body(default=..., alias="institution_address")
    campuses: List[Union[campusInfoBasic, None]] = Body(default=[None], exclude_unset=True, alias="associated_campuses")
    prov: Union[provider, str] = Body(default="Deprecated", exclude_unset=True, alias="provider")

class nestedBuilding(BaseModel):
    name: str = Body(default=..., alias="building_name")
    address: str = Body(default=..., alias="building_address")
    consumption: float = Body(default=..., alias="total_energy_consumption")
    manager: str = Body(default=..., alias="building_manager")

class newCampus(BaseModel):
    name: str = Body(default=..., alias="campus_name")
    buildings: List[Union[nestedBuilding, None]] = Body(default=[], exclude_unset=True, alias="associated_buildings")
    prov: Union[provider, str] = Body(default="Deprecated", exclude_unset=True, alias="provider")
    address: str = Body(default=..., alias="campus_address")

class Room(BaseModel):
    length: int = Body(alias="room_length", default=...)
    width: int = Body(alias="room_width", default=...)
    height: int = Body(alias="room_height", default=...)
    space: int = Body(alias="max_occupancy", default=...)
    temp: str = Body(alias="desired_room_temp", default=...)
    number: int = Body(alias="room_number", default=...)

class newBuilding(BaseModel):
    name:str = Body(default=..., alias="building_name")
    address: str = Body(default=..., alias="building_address")
    rooms: Union[List[Room], List[None]] = Body(default=[None], exclude_unset=True)
    consumption: float = Body(default=..., alias="total_energy_consumption")
    manager: str = Body(default=..., alias="building_manager_id")




@app.post("/institutions", summary="Create a new Institution")
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
                {
                    "campus_name": "<campus_name>"
                    "campus_address": "<campus_address>"
                }
            ]
        }
    """
    newInstitute = apiServices.institutionCreation(institutionInfo.name, institutionInfo.prov, institutionInfo.campuses)
    if not newInstitute:
        raise HTTPException(status_code=404, detail="Failed to create institution!")
    return newInstitute

@app.get("/institutions", summary="Get all institutions")
async def getAllInstitutions():
    allInstitutions = apiServices.getAllInstitutions()
    if not allInstitutions:
        raise HTTPException(status_code=404, detail="No institutions present.")
    return allInstitutions


@app.post("/institutions/{institution_id}/campuses", summary="Creates a new campus")
async def createNewCampus(institution_id,campusInfo: newCampus=Body(examples={"Successful Post": c._NEW_CAMPUS})):
    newCampus = apiServices.campusCreation(campusInfo.name, campusInfo.address,
                                                   campusInfo.buildings, institution_id)
    if not newCampus:
        raise HTTPException(status_code=404, detail="Failed to create campus!")
    return newCampus

#@app.get("/insititutions/{institution_id}/campuses", summary="Get all campuses from Institution")
#async def getAllInstitutionCampuses(institution_id):
 #   campusInfo = apiServices.getCampuses(institution_id)
  #  if not campusInfo:
   #     raise HTTPException(status_code=404, detail="Could not find institution")
    #return campusInfo

@app.get("/institutions/{institution_id}", summary="Get institution information")
async def getInstitute(institution_id:str):
    institute = apiServices.getInstitution(institute_id=institution_id)
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    return institute

@app.get("/institutions/{institution_id}/campuses/{campus_id}", summary="Gets a single campus information")
async def getCampus(institution_id:str, campus_id:str):
    campus = apiServices.getCampus(institution_id=institution_id, campus_id=campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    return campus

@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}", summary="gets a specific buildings information", deprecated=True)
async def getBuilding(institution_id:str, campus_id:str, building_id):
    buildings = apiServices.getBuilding(institution_id=institution_id, campus_id=campus_id, building_id=building_id)
    if not buildings:
        raise HTTPException(status_code=404, detail="Buildings not found")
    return buildings

@app.get("/institutions/{institution_id}/campuses", summary="gets all campuses associated with an institution")
async def getAllCampuses(institution_id:str):
    campuses = apiServices.getCampuses(institution_id=institution_id)
    if not campuses:
        raise HTTPException(status_code=404, detail="Institution not found")
    return campuses

@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings", summary="gets all buildings associated with a campus")
async def getAllBuildings(institution_id:str, campus_id:str):
    buildings = apiServices.getBuildings(institution_id=institution_id, campus_id=campus_id)
    if not buildings:
        raise HTTPException(status_code=404, detail="Buildings not found")
    return buildings



@app.post("/institutions/{institution_id}/campus/{campus_id}/buildings",summary="Create a new building")
async def newBuilding(institution_id:str, campus_id:str, buildingInfo: newBuilding=Body(
                                examples={"Succesful Post": c._NEW_BUILDINGS})):
    building = apiServices.buildingCreation(instituteId=institution_id, name=buildingInfo.name, address=buildingInfo.address,
                                            rooms=buildingInfo.rooms, consumption=buildingInfo.consumption,
                                            manager=buildingInfo.manager, campus_id=campus_id)
    if not building:
        raise HTTPException(status_code=404, detail="Failed to create the building!")
    return building


@app.post("/institutions/{institution_id}/users", summary="Creates a new user", deprecated=True)
async def createNewUser(userInfo: newUser, institution_id: str):
    newUser = apiServices.userCreation(institute=institution_id, name=(userInfo.first_name, userInfo.last_name),
                        email=userInfo.email, password=userInfo.password, pin=userInfo.pin)
    if not newUser:
        raise HTTPException(status_code=404, detail="Failed to create user!")
    return newUser


@app.post("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}/rooms",
          summary="Creates a new room")
async def addRoomInformation(institution_id, campus_id, building_id, room:Room = Body(
    examples={"Succesful Post": c._NEW_ROOM})):
    newRoom = apiServices.createNewRoom(institution_id=institution_id, campus_id=campus_id, building_id=building_id,
                                        room=room)
    if not room:
        raise HTTPException(status_code=404, detail="Failed to create room")
    return newRoom


@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}/rooms", summary="Get all rooms associated with a buidling", deprecated=True)
async def getAllRoomsInformation(institution_id:str, campus_id:str, building_id:str):
    building_rooms = apiServices.get_all_rooms(institution_id, campus_id, building_id)
    if not building_rooms:
        raise HTTPException(status_code=404, detail="Building not found")
    return building_rooms


@app.get("/institutions/{institution_id}/campuses/{campus_id}/buildings/{building_id}/rooms/{room_id}", summary="Get specific room information",deprecated=True)
async def getRoomInfo(institution_id:str, campus_id:str, building_id:str, room_id:str):
    pass


@app.get("/institutions/{institution_id}/users", summary="Get all user information", deprecated=True)
async def getAllUsers(institution_id:str):
    pass


@app.get("/institutions/{institution_id}/users/{user_id}", summary="Get user information", deprecated=True)
async def getUserInfo(institution_id:str, user_id:str):
    pass


