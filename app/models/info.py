from app.main import get_settings

SETTINGS = get_settings()

class Info:
    app_name = SETTINGS.app_name
    developer_email = SETTINGS.developer_email
