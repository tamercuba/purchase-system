import pytest
from domain.entities import Sale, SaleStatus
from pydantic import ValidationError

# pylint: disable=redefined-outer-name, too-many-arguments


@pytest.fixture
def sale_data():
    return {
        'code': 'ABC',
        'value': 120.00,
        'date': '2020-09-01',
        'salesman_cpf': '123',
    }


@pytest.fixture
def sale(sale_data) -> Sale:
    return Sale(**sale_data)


class TestSaleEntity:
    def test_create_complete_sale(self, sale_data):
        data = {**sale_data, 'status': SaleStatus.APPROVED}
        sale = Sale(**data)

        assert sale

    @pytest.mark.parametrize(
        'wrong_status,error',
        [
            (1, 'SaleStatus needs to be a string'),
            ('carlos', 'Invalid SaleStatus, valids:'),
        ],
    )
    def test_sale_wrong_statuses(self, wrong_status, error, sale_data):
        data = {**sale_data, 'status': wrong_status}
        with pytest.raises(ValidationError) as e:
            Sale(**data)
            assert error in e

    @pytest.mark.parametrize(
        'pre_status,method_name,post_status',
        [
            (SaleStatus.VALIDATING, 'approve', SaleStatus.APPROVED),
            (SaleStatus.VALIDATING, 'repprove', SaleStatus.REPPROVED),
        ],
    )
    def test_update_status(
        self, pre_status: str, method_name: str, post_status: str, sale: Sale
    ):
        assert sale.status == pre_status
        getattr(sale, method_name)()
        assert sale.status == post_status


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
def test_sale_cashback_value(
    sale: Sale, expected_cashback_value: float, expected_cashback_total: float
):
    assert sale.cashback.value == expected_cashback_value
    assert sale.cashback.total == expected_cashback_total
