from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.services.user_service import UserService
from app.schemas.token import Token

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_service = UserService()
    return user_service.auth_user(form_data.username, form_data.password)
