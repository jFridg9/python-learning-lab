import pytest
from zybooks.division_three import three_floor_divs


def test_three_floor_divs_positive():
    assert three_floor_divs(100, 3) == (33, 11, 3)


def test_three_floor_divs_negative():
    # floor division with negatives rounds toward -inf
    assert three_floor_divs(-100, 3) == (-34, -12, -4)


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        three_floor_divs(10, 0)
