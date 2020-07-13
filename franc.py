import money


class Franc(money.Money):
    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
