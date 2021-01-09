import time
from unittest import TestCase
from unittest.mock import patch

class Calculator:
    def sum(self, a, b):
        time.sleep(10) # long running process
        return a + b

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)
