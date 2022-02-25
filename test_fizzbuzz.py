from unittest import TestCase
from fizzbuzz import fizzBuzz

class Test(TestCase):
    def test_fizz_buzz(self):
        for i in [15]:
            self.assertTrue(fizzBuzz(i))

    def test_fizz(self):
        for i in [3]:
            assert fizzBuzz(i) == "Fizz"

    def test_buzz(self):
        for i in [5]:
            assert fizzBuzz(i) == "Buzz"

    def test_i(self):
        for i in range(1, 101):
            assert fizzBuzz(i)

