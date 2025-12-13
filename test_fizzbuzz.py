# test_fizzbuzz.py
# from fizzbuzz import fizzbuzz
from fizzbuzz import says
from unittest import mock

# def test_returns_number_as_string():
#     assert fizzbuzz(1) == "1"
#     assert fizzbuzz(2) == "2"
#     assert fizzbuzz(4) == "4"

# def test_returns_fizz_for_multiples_of_three():
#     assert fizzbuzz(3) == "Fizz"
#     assert fizzbuzz(6) == "Fizz"
#     assert fizzbuzz(9) == "Fizz"
#     assert fizzbuzz(12) == "Fizz"

# def test_returns_buzz_for_multiples_of_five():
#     assert fizzbuzz(5) == "Buzz"
#     assert fizzbuzz(10) == "Buzz"


# def test_returns_fizzbuzz_for_multiples_of_three_and_five():
#     assert fizzbuzz(15) == "FizzBuzz"
#     assert fizzbuzz(30) == "FizzBuzz"


def test_says():
    with mock.patch("fizzbuzz.print") as print_:
        with mock.patch("fizzbuzz.to_string", side_effect=["1"] * 15):
            # 1, 2 ... 15
            says(list(range(1, 16)))

    assert print_.call_count == 15


def test_says_will_print_fizzbuzz_return():
    return_value = "x"
    with mock.patch("fizzbuzz.print") as print_:
        with mock.patch("fizzbuzz.fizzbuzz", return_value=return_value) as fb:
            # [1, 2]
            says(list(range(1, 3)))
    calls = [mock.call(return_value), mock.call(return_value)]
    print_.assert_has_calls(calls)