class Dollar:
    amount: int

    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        self.amount = self.amount * multiplier
