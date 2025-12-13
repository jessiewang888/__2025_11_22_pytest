# def fizzbuzz(number):
#     return(
#         ("Fizz" if number % 3 == 0 else "")
#         + ("Buzz" if number % 5 == 0 else "")
#     )or str(number)

import time


def to_string(n, a, b, c):
    time.sleep(1)
    return str(n)


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return to_string(n)


def says(numbers: list[int]):
    '''
    list[number] -> print(fizzbuzz(number))
    val = fizzbuzz(number)
    print(val)
    '''
    for number in numbers:
        print(fizzbuzz(number))