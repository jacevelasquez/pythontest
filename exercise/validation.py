from pydantic import BaseModel

# validation (insert) for request data
class ItemCreate(BaseModel):
    name: str
    description: str
    longitude: float
    latitude: float
 
# validation for response data
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    longitude: float
    latitude: float

# validation (areas) for request data
class AreasCovered(BaseModel):
    distance: float
    longitude: float
    latitude: float