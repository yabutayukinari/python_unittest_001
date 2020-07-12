class Dollar:
    __amount: int

    def __init__(self, amount: int):
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def equals(self, object):
        dollar = object
        return self.__amount == dollar.__amount

    def __eq__(self, money):
        return self.__amount == money.__amount
