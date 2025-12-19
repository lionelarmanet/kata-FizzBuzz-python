import pytest

from src.main import FizzBuzz

def test_sample():
    assert 1 + 1 == 2


def test_another_sample():
    assert True is True

@pytest.mark.parametrize(
    "number, expected",
    [
        (1,"1"),
        (2,"2"),
        (3,"Fizz")
    ])
def test_fizz_buzz(number:int, expected:str):
    assert FizzBuzz(number) == expected