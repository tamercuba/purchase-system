from fastapi import APIRouter

from api.controllers import create_sale, get_token, register

router = APIRouter()
router.include_router(create_sale.router)
router.include_router(get_token.router)
router.include_router(register.router)
