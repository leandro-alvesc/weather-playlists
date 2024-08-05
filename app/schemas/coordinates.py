from pydantic import BaseModel

class Coordinates(BaseModel):
    name: str
    state: str | None
    country: str
    latitude: str
    longitude: str
