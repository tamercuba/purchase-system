import pytest
from core.entities.sale import Sale
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
            assert error in e.__str__()

    def test_sale_status_special_rule(self, sale: Sale, sale_data):
        assert sale.status == 'validating'

        sale = Sale(**{**sale_data, 'salesman_cpf': '15350946056'})

        assert sale.status == 'approved'

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

    @pytest.mark.parametrize(
        'value,expected_cashback,expected_cashback_result',
        [
            (900, 0.1, 90),
            (1000, 0.1, 100),
            (1001, 0.15, 150.15),
            (1500, 0.15, 225),
            (1501, 0.2, 300.2),
        ],
    )
    def test_check_cashback(
        self, value, expected_cashback, expected_cashback_result, sale_data
    ):
        data = {**sale_data, 'value': value}
        sale = Sale(**data)

        assert sale.cashback == expected_cashback
        assert sale.cashback_result == expected_cashback_result
