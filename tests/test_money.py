import unittest

import Dollar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        five = Dollar.Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)


if __name__ == '__main__':
    unittest.main()
