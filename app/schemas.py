from pydantic import BaseModel
from pydantic import ConfigDict
class ProjectBase(BaseModel):
    name: str
    location: str
    lat: float
    lng: float
    price: float
    description: str
    category: str
    image_url: str

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int

class Config:
    model_config = ConfigDict(from_attributes=True)