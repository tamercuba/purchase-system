from fastapi import APIRouter

from api.routes import create_sale, get_token

router = APIRouter()
router.include_router(get_token.router, tags=['get_token'])
router.include_router(create_sale.router, tags=['create_sale'])
