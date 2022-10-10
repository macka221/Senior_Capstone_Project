from fastapi import FastAPI, HTTPException, Body
from starlette.responses import Response
from pydantic import BaseModel
from app.api.downstreamServices.downstreamService import businessServices
from typing import List

app = FastAPI()

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

@app.post("/app/institutions")
async def newInstitution(institutionInfo: newInstitution):
    newInstitute = businessServices.institutionCreation(name=institutionInfo.name, address=institutionInfo.address,
                                                campuses=institutionInfo.campuses)
    if not newInstitute:
        raise HTTPException(status_code=404, detail="Failed to create institution!")
    return {"message": "Institution Created Successfully"}

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

