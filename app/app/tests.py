"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_num(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_num(self):
        res = calc.subtract(6, 1)
        self.assertEqual(res, -5)
