from adapters.api.services import authenticate_service, delete_sale_service
from fastapi import APIRouter, Depends, Response, status
from fastapi_jwt_auth import AuthJWT

router = APIRouter()


@router.delete('/sale/{sale_id}')
def delete_sale(sale_id: str, auth: AuthJWT = Depends()) -> None:
    user = authenticate_service(auth)
    delete_sale_service.handle({'sale_id': sale_id, 'salesman': user})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
