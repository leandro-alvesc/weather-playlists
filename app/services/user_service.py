from fastapi import HTTPException
from firedantic import ModelNotFoundError

from app.logger import get_logger
from app.schemas.user import UserInput
from app.schemas.token import Token
from app.models.user import User
from app.utils.auth_utils import AuthUtils

LOGGER = get_logger()


class UserService:
    @classmethod
    def get_user_by_email(cls, email: str) -> User:
        return User.get_user_by_email(email)

    @classmethod
    def auth_user(cls, email, password) -> Token:
        user = User.get_user_by_email(email)

        if not AuthUtils.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=400, detail='Invalid credentials.')
        return Token(access_token=AuthUtils.create_access_token(user.email))

    @classmethod
    def create_user(cls, user_input: UserInput) -> User:
        if User.exists_user(user_input.email):
            raise HTTPException(status_code=400, detail='User already exists.')

        created_user = User(
            name=user_input.name,
            email=user_input.email,
            hashed_password=AuthUtils.hash_password(user_input.password))
        created_user.save()
        return created_user.to_schema()
