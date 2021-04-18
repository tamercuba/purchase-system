from fastapi import APIRouter, FastAPI

import api.settings as settings
from api.router import router


def get_app() -> FastAPI:
    _app = FastAPI(debug=settings.APP_DEBUG)
    _app.include_router(router)
    return _app

app = get_app()
