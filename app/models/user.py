from fastapi import HTTPException
from typing import Self

from app.models.base_firestore_model import FirestoreBaseModel
from app.schemas.user import UserOutput


class User(FirestoreBaseModel):
    __collection__ = 'users'
    name: str
    email: str
    hashed_password: str

    @classmethod
    def get_user_by_email(cls, email: str) -> Self:
        user = cls.find_one_or_none(dict(email=email))
        if not user:
            raise HTTPException(status_code=404, detail='User not found.')
        return user

    @classmethod
    def exists_user(cls, email: str) -> bool:
        return bool(cls.find_one_or_none(dict(email=email)))

    def to_schema(self) -> UserOutput:
        return UserOutput(name=self.name, email=self.email)
