from functools import partial


def is_multiple_of(number: int, divisor: int) -> bool:
    return number % divisor == 0


is_multiple_of_3 = partial(is_multiple_of, divisor=3)
is_multiple_of_5 = partial(is_multiple_of, divisor=5)
is_multiple_of_3_and_5 = partial(is_multiple_of, divisor=3 * 5)


def FizzBuzz(number: int) -> str:
    if is_multiple_of_3_and_5(number):
        return "FizzBuzz"
    if is_multiple_of_3(number):
        return "Fizz"
    if is_multiple_of_5(number):
        return "Buzz"
    return str(number)
