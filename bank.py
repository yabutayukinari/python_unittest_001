class Bank:
    rates = dict()

    def reduce(self, source, to: str):
        return source.reduce(self, to)

    def add_rate(self, from_currency: str, to_currency: str, rate: int):

        self.rates[(from_currency, to_currency)] = rate

    def rate(self, from_currency: str, to_currency: str):
        if from_currency == to_currency:
            return 1
        return self.rates[(from_currency, to_currency)]
