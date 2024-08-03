from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from app.services.user_service import UserService
from app.schemas.user import UserOutput, UserInput
from app.utils.auth_utils import AuthUtils

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me', response_model=UserOutput)
def get_me(email: Annotated[str, Depends(AuthUtils.get_user_email_from_token)]):
    user_service = UserService()
    return user_service.get_user_by_email(email).to_schema()


@router.post('/', response_model=UserOutput)
def create_user(user: UserInput):
    user_service = UserService()
    return user_service.create_user(user).to_schema()
