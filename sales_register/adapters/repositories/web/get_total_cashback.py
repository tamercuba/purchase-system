import json

import requests
from .settings import settings
from shared.exceptions import EntityNotFound


class GetTotalCashback:
    def total_salesman_cashback(self, cpf: str) -> float:
        url = settings.API_URL + cpf
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise EntityNotFound(
                'An error occured when fetching total cashback',
                info={'status_code': response.status_code, 'cpf': cpf},
            )

        value = json.loads(response.content)

        return value['body']['credit']

    @property
    def headers(self):
        return {'Authorization': settings.REQUEST_TOKEN}
