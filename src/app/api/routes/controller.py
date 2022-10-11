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

# TODO: Create endpoints for adding room information and campus information.
@app.post("/app/institutions/{institutionId}/users")
async def createNewUser(userInfo: newUser, institutionId: str):
    newUser = businessServices.userCreation(institution=institutionId, name=userInfo.name, email=userInfo.email,
                                    manager=userInfo.manager)
    if not newUser:
        raise HTTPException(status_code=404, detail="Failed to create user!")
    return {"message": "User created Successfully"}

