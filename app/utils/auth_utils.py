import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Header
from typing import Annotated

from jwt.exceptions import InvalidTokenError

from app.config import get_settings
from app.logger import get_logger

SETTINGS = get_settings()
LOGGER = get_logger()


class AuthUtils:
    @staticmethod
    def hash_password(password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password=pwd_bytes, salt=salt)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        pwd_bytes = password.encode('utf-8')
        hashed_pwd_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password=pwd_bytes,
                              hashed_password=hashed_pwd_bytes)

    @staticmethod
    def create_access_token(email: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=SETTINGS.jwt_access_token_expire_minutes)
        to_encode = dict(sub=email, exp=expire)

        return jwt.encode(to_encode, SETTINGS.jwt_secret_key,
                          algorithm=SETTINGS.jwt_algorithm)

    @staticmethod
    def get_user_email_from_token(token: Annotated[str, Header()]) -> str:
        email = None
        try:
            payload = jwt.decode(token, SETTINGS.jwt_secret_key,
                                 algorithms=[SETTINGS.jwt_algorithm])
            email = payload.get('sub')
        except InvalidTokenError as e:
            LOGGER.error(e)
            email = None

        if email is None:
            raise HTTPException(
                status_code=400, detail='Could not validate token')
        return email

                
        
