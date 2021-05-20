from adapters.api.authentication.config import User
from adapters.api.services import authenticate_service, delete_sale_service
from fastapi import APIRouter, Depends, Response, status

router = APIRouter()


@router.delete('/sale/{sale_id}')
def delete_sale(
    sale_id: str, user: User = Depends(authenticate_service)
) -> None:
    delete_sale_service.handle({'sale_id': sale_id, 'salesman': user})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
