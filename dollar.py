import money


class Dollar(money.Money):

    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)
