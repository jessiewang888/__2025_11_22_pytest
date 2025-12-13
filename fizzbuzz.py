# def fizzbuzz(number):
#     return(
#         ("Fizz" if number % 3 == 0 else "")
#         + ("Buzz" if number % 5 == 0 else "")
#     )or str(number)


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
