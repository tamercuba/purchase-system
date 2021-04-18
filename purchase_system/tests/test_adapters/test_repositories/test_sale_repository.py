from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import Sale


def test_get_sale(sale: Sale):
    repo = SaleRepository(initial_values=[sale])

    result = repo.get_by_id(_id=sale.id)

    assert result == sale
