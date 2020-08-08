import pytest

from all_your_base import rebase


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0


def test_single_bit_to_one_decimal():
    assert [1] == rebase(2, [1], 10)


def test_binary_to_single_decimal():
    assert [5] == rebase(2, [1, 0, 1], 10)


def test_single_decimal_to_binary():
    assert [1, 0, 1] == rebase(10, [5], 2)


def test_binary_to_multiple_decimal():
    assert [4, 2] == rebase(2, [1, 0, 1, 0, 1, 0], 10)


def test_decimal_to_binary():
    assert [1, 0, 1, 0, 1, 0] == rebase(10, [4, 2], 2)


def test_trinary_to_hexadecimal():
    assert [2, 10] == rebase(3, [1, 1, 2, 0], 16)


def test_hexadecimal_to_trinary():
    assert [1, 1, 2, 0] == rebase(16, [2, 10], 3)


def test_15_bit_integer():
    assert [6, 10, 45] == rebase(97, [3, 46, 60], 73)


def test_empty_list():
    assert [] == rebase(2, [], 10)


def test_single_zero():
    assert [] == rebase(10, [0], 2)


def test_multiple_zeroes():
    assert [] == rebase(10, [0, 0, 0], 2)


def test_leading_zeros():
    assert [4, 2] == rebase(7, [0, 6, 0], 10)


def test_input_base_is_one():
    with pytest.raises(ValueError):
        rebase(1, [0], 10)


def test_input_base_is_zero():
    with pytest.raises(ValueError):
        rebase(0, [], 10)


def test_input_base_is_negative():
    with pytest.raises(ValueError):
        rebase(-2, [1], 10)


def test_negative_digit():
    with pytest.raises(ValueError):
        rebase(2, [1, -1, 1, 0, 1, 0], 10)


def test_invalid_positive_digit():
    with pytest.raises(ValueError):
        rebase(2, [1, 2, 1, 0, 1, 0], 10)


def test_output_base_is_one():
    with pytest.raises(ValueError):
        rebase(2, [1, 0, 1, 0, 1, 0], 1)


def test_output_base_is_zero():
    with pytest.raises(ValueError):
        rebase(10, [7], 0)


def test_output_base_is_negative():
    with pytest.raises(ValueError):
        rebase(2, [1], -7)


def test_both_bases_are_negative():
    with pytest.raises(ValueError):
        rebase(-2, [1], -7)
