from firedantic import Model

from app.schemas.user import UserOutput


class User(Model):
    __collection__ = "users"
    name: str
    email: str
    hashed_password: str

    def to_schema(self):
        return UserOutput(name=self.name, email=self.email)
