from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)   # Puede ser una dirección o coordenadas en formato "lat,lng"
    lat = Column(Float)                       # Latitud
    lng = Column(Float)                       # Longitud
    price = Column(Float)
    description = Column(String)
    category = Column(String)                 # Tipo de propiedad, por ejemplo: "residencial", "comercial"
    image_url = Column(String)                # URL de la imagen representativa