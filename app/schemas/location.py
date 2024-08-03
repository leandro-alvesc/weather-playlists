from pydantic import BaseModel

class Location(BaseModel):
    city_name: str
    state_code: str
    country_code: str
