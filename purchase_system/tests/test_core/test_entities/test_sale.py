import pytest
from core.entities import Sale
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
        data = {**sale_data, 'status': 'approved'}
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
            ('validating', 'approve', 'approved'),
            ('validating', 'repprove', 'repproved'),
        ],
    )
    def test_update_status(
        self, pre_status: str, method_name: str, post_status: str, sale: Sale
    ):
        assert sale.status == pre_status
        getattr(sale, method_name)()
        assert sale.status == post_status
