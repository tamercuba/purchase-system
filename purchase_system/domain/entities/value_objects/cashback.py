from shared.entities import ValueObject


class Cashback(ValueObject):
    sale_value: float

    @property
    def value(self) -> float:
        if self.sale_value <= 1000:
            return 0.1

        if self.sale_value <= 1500:
            return 0.15

        return 0.2

    @property
    def total(self) -> float:
        return self.value * self.sale_value
