import pytest
from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import Sale


@pytest.mark.asyncio
async def test_get_sale(sale: Sale):
    repo = SaleRepository(initial_values=[sale])

    result = await repo.get_by_id(_id=sale.id)

    assert result == sale
