from expression import Expression


class Money(Expression):
    _amount: int
    _currency: str

    def __init__(self, amount: int, currency=""):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend) -> Expression:
        return Money(self._amount + addend._amount, self._currency)

    def currency(self) -> str:
        return self._currency

    def equals(self, money) -> bool:
        return self._amount == money._amount and self.currency().__eq__(money.currency())

    def __eq__(self, money) -> bool:
        return self._amount == money._amount and self.currency().__eq__(money.currency())

    @staticmethod
    def dollar(amount: int):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount, "CHF")

    def __str__(self):
        return str(self._amount) + " " + self._currency

    __unicode__ = __str__
    __repr__ = __str__
