# from franc import Franc
from abc import ABCMeta, abstractmethod


class Money(object):
    _amount: int

    @abstractmethod
    def times(self, multiplier: int):
        raise NotImplementedError

    def equals(self, money) -> bool:
        return self._amount == money._amount and self.__class__.__name__ == money.__class__.__name__

    def __eq__(self, money) -> bool:
        return self._amount == money._amount and self.__class__.__name__ == money.__class__.__name__

    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)

    @staticmethod
    def franc(amount: int):
        return Franc(amount)


class Dollar(Money):
    """
    別ファイルで定義すると読み込んでくれないので避難
    """

    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int) -> Money:
        return Dollar(self._amount * multiplier)


class Franc(Money):
    """
    別ファイルで定義すると読み込んでくれないので避難
    """

    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
