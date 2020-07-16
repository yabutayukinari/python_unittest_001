import unittest
from money import Money
from money import Sum
from bank import Bank


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        """
        掛け算テスト
        :return:
        """
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        """
        等価テスト
        :return:
        """
        self.assertTrue(Money.dollar(5).equals(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).equals(Money.dollar(6)))
        self.assertFalse(Money.franc(5).equals(Money.dollar(5)))

    def test_currency(self):
        """
        通貨単位テスト
        :return:
        """
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        """
        足し算テスト
        :return:
        """
        five = Money.dollar(5)
        cul_sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(cul_sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five: Money = Money.dollar(5)
        result = five.plus(five)
        cul_sum = result
        self.assertEqual(five, cul_sum.augend)
        self.assertEqual(five, cul_sum.addend)

    def test_reduce_sum(self):
        cul_sum = Sum(Money.dollar(3), Money.dollar(4))
        bank: Bank = Bank()
        result: Money = bank.reduce(cul_sum, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank: Bank = Bank()
        result: Money = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank: Bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result: Money = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)


if __name__ == '__main__':
    unittest.main()
