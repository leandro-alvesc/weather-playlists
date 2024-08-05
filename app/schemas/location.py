from pydantic import BaseModel

class Location(BaseModel):
    city_name: str
    country_code: str
