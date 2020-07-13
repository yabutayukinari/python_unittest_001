import unittest

import dollar
import franc


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five = dollar.Dollar(5)
        self.assertEqual(dollar.Dollar(10), five.times(2))
        self.assertEqual(dollar.Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(dollar.Dollar(5).equals(dollar.Dollar(5)))
        self.assertFalse(dollar.Dollar(5).equals(dollar.Dollar(6)))
        self.assertTrue(franc.Franc(5).equals(franc.Franc(5)))
        self.assertFalse(franc.Franc(5).equals(franc.Franc(6)))
        self.assertFalse(franc.Franc(5).equals(dollar.Dollar(5)))

    def test_franc_multiplication(self):
        five = franc.Franc(5)
        self.assertEqual(franc.Franc(10), five.times(2))
        self.assertEqual(franc.Franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
