class Franc:
    __amount: int

    def __init__(self, amount: int):
        self.__amount = amount

    def times(self, multiplier: int):
        return Franc(self.__amount * multiplier)

    def equals(self, object):
        franc = object
        return self.__amount == franc.__amount

    def __eq__(self, money):
        return self.__amount == money.__amount
