from pydantic import BaseModel

class Coordinates(BaseModel):
    name: str
    state: str
    country: str
    latitude: str
    longitude: str
