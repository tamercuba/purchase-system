from core.entities import Sale


class CashbackHandler:
    def __init__(self, sale: Sale):
        self._sale = sale

    @property
    def value(self) -> float:
        if self._sale.value <= 1000:
            return 0.1

        if self._sale.value <= 1500:
            return 0.15

        return 0.2

    @property
    def total(self) -> float:
        return self.value * self._sale.value
