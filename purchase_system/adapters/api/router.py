from adapters.api.controllers import (
    create_sale,
    delete_sale,
    get_token,
    get_user_cashback,
    list_sales,
    register,
    update_sale,
)
from fastapi import APIRouter

router = APIRouter()
router.include_router(create_sale.router)
router.include_router(get_token.router)
router.include_router(register.router)
router.include_router(list_sales.router)
router.include_router(delete_sale.router)
router.include_router(get_user_cashback.router)
router.include_router(update_sale.router)
