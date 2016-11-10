from app import logic

import unittest

class CalculatorTestCase(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(logic.calculator_add(5), 15)

    def test_numbers_less_than_one(self):
        self.assertEqual(logic.calculator_add(-5), 0)

    def test_value_is_integer(self):
        self.assertEqual(logic.calculator_add(""), "Only integers allowed")
