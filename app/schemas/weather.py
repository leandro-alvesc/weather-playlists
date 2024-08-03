from pydantic import BaseModel


class Weather(BaseModel):
    city: str
    name: str
    description: str
    temperature: float
    feels_like: float
    humidity: int
    
