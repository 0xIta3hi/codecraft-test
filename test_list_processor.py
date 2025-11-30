"""
test_list_processor.py - Test suite for list_processor.py

Tests list processing functions that have off-by-one errors.
Tests WILL FAIL with the current buggy code.
"""

import pytest
from list_processor import (
    remove_duplicates_preserve_order,
    calculate_moving_average,
    extract_subsequence
)


class TestRemoveDuplicates:
    """Test cases for remove_duplicates_preserve_order function."""
    
    def test_remove_duplicates_simple(self):
        """Test removing duplicates from simple list."""
        result = remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4])
        assert result == [1, 2, 3, 4], "Should remove all duplicates"
    
    def test_remove_duplicates_preserves_order(self):
        """Test that order is preserved when removing duplicates."""
        result = remove_duplicates_preserve_order([3, 1, 2, 1, 3])
        assert result == [3, 1, 2], "Should preserve original order"
    
    def test_remove_duplicates_last_element_not_skipped(self):
        """Test that the last element is NOT skipped (this fails with bug)."""
        # Bug: off-by-one causes last element to be skipped
        result = remove_duplicates_preserve_order([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5], "Should include all elements including last"
        assert len(result) == 5, "All 5 elements should be present"
    
    def test_remove_duplicates_duplicate_at_end(self):
        """Test with duplicate at the end (definitely gets skipped with bug)."""
        result = remove_duplicates_preserve_order([1, 2, 3, 2])
        assert result == [1, 2, 3], "Should include and deduplicate the last element"
        assert 2 not in result[2:], "Last duplicate should be removed"
    
    def test_remove_duplicates_single_element(self):
        """Test with single element list."""
        result = remove_duplicates_preserve_order([42])
        assert result == [42], "Single element should be preserved"
    
    def test_remove_duplicates_empty_list(self):
        """Test with empty list."""
        result = remove_duplicates_preserve_order([])
        assert result == [], "Empty list should return empty"


class TestMovingAverage:
    """Test cases for calculate_moving_average function."""
    
    def test_moving_average_simple(self):
        """Test moving average with simple values."""
        values = [1, 2, 3, 4, 5]
        result = calculate_moving_average(values, 2)
        expected = [1.5, 2.5, 3.5, 4.5]  # All windows of size 2
        assert result == expected, "Should calculate all moving averages"
    
    def test_moving_average_includes_last_window(self):
        """Test that the last valid window is included (fails with bug)."""
        values = [10, 20, 30, 40]
        result = calculate_moving_average(values, 2)
        # Should have 3 windows: [10,20], [20,30], [30,40]
        assert len(result) == 3, "Should have 3 windows for 4 values with window size 2"
        assert result[-1] == 35.0, "Last window average should be 35"
    
    def test_moving_average_window_size_1(self):
        """Test with window size of 1."""
        values = [5, 10, 15]
        result = calculate_moving_average(values, 1)
        assert result == [5.0, 10.0, 15.0], "Window size 1 should return all values"
    
    def test_moving_average_correct_count(self):
        """Test that the correct number of windows is returned."""
        values = [1, 2, 3, 4, 5, 6]
        window_size = 3
        result = calculate_moving_average(values, window_size)
        # For n=6 and window=3, should have 6-3+1=4 windows
        assert len(result) == 4, "Should have 4 windows"
        assert result == [2.0, 3.0, 4.0, 5.0]


class TestExtractSubsequence:
    """Test cases for extract_subsequence function."""
    
    def test_extract_subsequence_inclusive_end(self):
        """Test that end index is inclusive (API expectation)."""
        sequence = [1, 2, 3, 4, 5]
        # API should be inclusive on both ends
        result = extract_subsequence(sequence, 1, 3)
        # Expected: elements at indices 1, 2, 3 = [2, 3, 4]
        assert result == [2, 3, 4], "End index should be inclusive"
    
    def test_extract_subsequence_full_range(self):
        """Test extracting the full range."""
        sequence = [10, 20, 30, 40, 50]
        result = extract_subsequence(sequence, 0, 4)
        assert result == [10, 20, 30, 40, 50], "Should include all elements with inclusive end"
    
    def test_extract_subsequence_single_element(self):
        """Test extracting a single element."""
        sequence = [1, 2, 3, 4, 5]
        result = extract_subsequence(sequence, 2, 2)
        assert result == [3], "Should extract single element at index 2"
    
    def test_extract_subsequence_start_to_end(self):
        """Test various subsequence extractions."""
        sequence = ['a', 'b', 'c', 'd', 'e']
        
        # Extract indices 1 to 3 (inclusive)
        result = extract_subsequence(sequence, 1, 3)
        assert result == ['b', 'c', 'd'], "Should extract ['b', 'c', 'd']"
        assert len(result) == 3, "Should have 3 elements"
