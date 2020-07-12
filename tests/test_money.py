import unittest

import Dollar


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar.Dollar(5)
        self.assertEqual(Dollar.Dollar(10), five.times(2))
        self.assertEqual(Dollar.Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Dollar.Dollar(5).equals(Dollar.Dollar(5)))
        self.assertFalse(Dollar.Dollar(5).equals(Dollar.Dollar(6)))

if __name__ == '__main__':
    unittest.main()
