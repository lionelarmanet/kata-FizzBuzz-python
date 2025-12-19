import pytest

from src.main import FizzBuzz


def test_sample():
    assert 1 + 1 == 2


def test_another_sample():
    assert True is True


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (4, "4"),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, "7"),
        (8, "8"),
        (9, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
    ],
)
def test_fizz_buzz(number: int, expected: str):
    assert FizzBuzz(number) == expected

