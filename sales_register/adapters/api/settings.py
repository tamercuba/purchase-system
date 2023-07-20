from pydantic_settings import BaseSettings


class APISettings(BaseSettings):
    APP_HOST: str = 'localhost'
    APP_PORT: str = '8000'
    APP_DEBUG: bool = True
    SECRET_KEY: str = 'a'


api_settings = APISettings()
