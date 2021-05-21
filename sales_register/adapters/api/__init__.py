from adapters.api.router import router
from adapters.api.settings import APP_DEBUG
from fastapi import FastAPI


def get_app() -> FastAPI:
    _app = FastAPI(debug=APP_DEBUG)
    _app.include_router(router)
    return _app


app = get_app()
