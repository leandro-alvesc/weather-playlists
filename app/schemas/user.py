from pydantic import BaseModel, EmailStr, Field


class UserOutput(BaseModel):
    name: str
    email: EmailStr | None = Field(default=None)


class UserInput(UserOutput):
    password: str
