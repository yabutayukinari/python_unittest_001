import unittest

import Dollar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        five = Dollar.Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)


if __name__ == '__main__':
    unittest.main()
