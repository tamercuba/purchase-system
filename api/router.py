from fastapi import APIRouter

from api.controllers import create_sale, get_token, list_sales, register

router = APIRouter()
router.include_router(create_sale.router)
router.include_router(get_token.router)
router.include_router(register.router)
router.include_router(list_sales.router)
