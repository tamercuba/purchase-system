import pytest
from core.entities import Sale
from core.services import CashbackHandler


@pytest.mark.parametrize(
    'sale,expected_cashback_value,expected_cashback_total',
    [
        (
            Sale(
                **{
                    'code': 'a',
                    'value': 900,
                    'date': '1997-09-01',
                    'salesman_cpf': '123',
                }
            ),
            0.1,
            90,
        ),
        (
            Sale(
                **{
                    'code': 'a',
                    'value': 1000,
                    'date': '1997-09-01',
                    'salesman_cpf': '123',
                }
            ),
            0.1,
            100,
        ),
        (
            Sale(
                **{
                    'code': 'a',
                    'value': 1001,
                    'date': '1997-09-01',
                    'salesman_cpf': '123',
                }
            ),
            0.15,
            150.15,
        ),
        (
            Sale(
                **{
                    'code': 'a',
                    'value': 1500,
                    'date': '1997-09-01',
                    'salesman_cpf': '123',
                }
            ),
            0.15,
            225,
        ),
        (
            Sale(
                **{
                    'code': 'a',
                    'value': 1501,
                    'date': '1997-09-01',
                    'salesman_cpf': '123',
                }
            ),
            0.2,
            300.2,
        ),
    ],
)
def test_cashback_handler_values(
    sale: Sale, expected_cashback_value: float, expected_cashback_total: float
):
    handler = CashbackHandler(sale)

    assert handler.value == expected_cashback_value
    assert handler.total == expected_cashback_total
