import pytest

from src.util.util import get_nth_bit_from_left

test_data_five = [
    (0b101, 0, 1),
    (0b101, 1, 0),
    (0b101, 2, 1)
]

test_data_four = [
    (0b100, 0, 1),
    (0b100, 1, 0),
    (0b100, 2, 0)
]

test_data = test_data_five + test_data_four


@pytest.mark.parametrize("binary, n, expected", test_data)
def test_get_nth_bit_5(binary, n, expected):
    assert get_nth_bit_from_left(binary, n) == expected
