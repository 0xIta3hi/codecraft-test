"""
test_calc.py - Test suite for calc.py

Tests the calculate_average function, including edge cases.
Tests WILL FAIL with the current buggy code.
"""

import pytest
from calc import calculate_average


def test_calculate_average_normal_case():
    """Test average calculation with normal input."""
    result = calculate_average([1, 2, 3, 4, 5])
    assert result == 3.0


def test_calculate_average_single_element():
    """Test average calculation with a single element."""
    result = calculate_average([42])
    assert result == 42.0


def test_calculate_average_empty_list():
    """Test that empty list returns 0.0 instead of crashing."""
    # This test FAILS with current code (ZeroDivisionError)
    # It should return 0.0 or raise ValueError with proper message
    result = calculate_average([])
    assert result == 0.0


def test_calculate_average_negative_numbers():
    """Test average calculation with negative numbers."""
    result = calculate_average([-10, -5, 0, 5, 10])
    assert result == 0.0
