from pydantic_settings import BaseSettings


class WebSettings(BaseSettings):
    REQUEST_TOKEN: str = 'tamer'
    API_URL: str = 'http://localhost:8080'


settings = WebSettings()
