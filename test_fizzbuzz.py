# test_fizzbuzz.py
from fizzbuzz import fizzbuzz

def test_returns_number_as_string():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"

def test_returns_fizz_for_multiples_of_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(12) == "Fizz"

def test_returns_fizzbuzz_for_multiples_of_three_and_five():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_returns_fizzbuzz_for_multiples_of_three_and_five():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
