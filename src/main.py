def FizzBuzz(number: int) -> str:
    if number % 15 == 0:  # perf optimization for mod 3 and mod 5
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return f"{number}"
