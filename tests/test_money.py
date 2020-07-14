import unittest
from money import Money
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


if __name__ == '__main__':
    unittest.main()
