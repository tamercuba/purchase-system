from typing import Optional

from adapters.api.services import update_sale_service, validate_token_service
from adapters.api.services.authentication import User
from domain.services.exceptions import CantBeUpdated
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter()


class Request(BaseModel):
    code: str
    value: float
    date: str
    status: Optional[str]


class Response(Request):
    id: str


@router.put(
    '/sale/{sale_id}',
    status_code=status.HTTP_200_OK,
    response_model=Response,
)
def update_sale(
    sale_id: str,
    request: Request,
    user: User = Depends(validate_token_service),
) -> Response:
    try:
        result = update_sale_service.handle(
            {
                'sale_id': sale_id,
                'salesman': user,
                'sale': {
                    'code': request.code,
                    'value': request.value,
                    'date': request.date,
                    'status': request.status,
                },
            }
        )

        return Response(
            **{
                'id': result.id,
                'code': result.code,
                'value': result.value,
                'date': str(result.date),
                'status': result.status,
            }
        )
    except CantBeUpdated as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=e.reason
        )
