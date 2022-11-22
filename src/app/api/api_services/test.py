from app.api.api_services.energy import *
from app.api.api_services.buildings import building, room

newRoom = room(temp=rm.temp, length=rm.length, width=rm.width, height=rm.height, max_occupancy=rm.space,
                       room_number=rm.number)
newBuilding = building(name="dansby", address="water", manager="brandon", consumption=1, rooms=[])