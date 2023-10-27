"""
Sample Test
"""
from django.test import SimpleTestCase
from app import calc


class TestCalculator(SimpleTestCase):
    """Test the calc module."""

    def test_add(self):
        """Test adding x to y"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtracting_numbers(self):
        """Test subtracting x from y"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
