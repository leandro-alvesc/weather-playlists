from pydantic import BaseModel

from app.config import get_settings

SETTINGS = get_settings()


class Info(BaseModel):
    app_name: str = SETTINGS.app_name
    developer_email: str = SETTINGS.developer_email
