import pytest

from generator import EvenGenerator


def test_that_first_is_included_last_is_excluded():
    assert list(EvenGenerator(2, 6)) == [2, 4]


def test_that_generator_can_handle_negative_numbers():
    assert list(EvenGenerator(-2, 4)) == [-2, 0, 2]


def test_that_generator_generates_in_descending_order():
    assert list(EvenGenerator(4, -2)) == [4, 2, 0]
    assert list(EvenGenerator(6, 2)) == [6, 4]
    assert list(EvenGenerator(7, 2)) == [6, 4]
