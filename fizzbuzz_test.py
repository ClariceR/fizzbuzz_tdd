import pytest
import fizzbuzz


def test_number_is_divisible_by_three():
    assert fizzbuzz.is_divisible_by(3, 3)


def test_number_is_NOT_divisible_by_three():
    assert not fizzbuzz.is_divisible_by(1, 3)


def test_number_is_divisible_by_five():
    assert fizzbuzz.is_divisible_by(5, 5)


def test_number_is_NOT_divisible_by_five():
    assert not fizzbuzz.is_divisible_by(1, 5)


def test_say_fizz():
    assert fizzbuzz.say(3) == 'fizz'


def test_say_buzz():
    assert fizzbuzz.say(5) == 'buzz'


def test_say_fizzbuzz():
    assert fizzbuzz.say(15) == 'fizzbuzz'


def test_return_number():
    assert fizzbuzz.say(11) == 11
