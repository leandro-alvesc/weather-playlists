from pydantic import BaseModel, EmailStr, Field


class UserOutput(BaseModel):
    name: str
    email: EmailStr = Field()


class UserInput(UserOutput):
    password: str
