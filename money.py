class Money:
    _amount: int

    def equals(self, money) -> bool:
        return self._amount == money._amount and self.__class__.__name__ == money.__class__.__name__

    def __eq__(self, money) -> bool:
        return self._amount == money._amount and self.__class__.__name__ == money.__class__.__name__

