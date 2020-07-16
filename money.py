from expression import Expression
from bank import Bank

class Money(Expression):
    _amount: int
    _currency: str

    def __init__(self, amount: int, currency=""):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend) -> Expression:
        return Sum(self, addend)

    def currency(self) -> str:
        return self._currency

    def reduce(self, bank: Bank, to: str):
        rate: int = bank.rate(self._currency, to)
        return Money(int(self._amount / rate), to)

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


class Sum(Expression):
    augend: Money
    addend: Money

    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend
        pass

    def reduce(self, bank: Bank, to: str):
        amount: int = self.augend._amount + self.addend._amount
        return Money(amount, to)
