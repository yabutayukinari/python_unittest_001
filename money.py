# from franc import Franc
from abc import ABCMeta, abstractmethod


class Money(object):
    _amount: int
    _currency: str

    def __init__(self, amount: int, currency=""):
        self._amount = amount
        self._currency = currency

    @abstractmethod
    def times(self, multiplier: int):
        raise NotImplementedError

    def currency(self) -> str:
        return self._currency

    def equals(self, money) -> bool:
        return self._amount == money._amount and self.__class__.__name__ == money.__class__.__name__

    def __eq__(self, money) -> bool:
        return self._amount == money._amount and self.__class__.__name__ == money.__class__.__name__

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int):
        return Franc(amount, "CHF")


class Dollar(Money):
    """
    別ファイルで定義すると読み込んでくれないので避難
    """
    def __init__(self, amount: int, currency):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    """
    別ファイルで定義すると読み込んでくれないので避難
    """
    def __init__(self, amount: int, currency):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)
