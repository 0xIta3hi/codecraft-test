"""
list_processor.py - Module with a subtle off-by-one error

This module processes lists and performs operations on their elements.
The bug: Loop boundary is off by one, skipping the last element or accessing beyond bounds.
"""


def remove_duplicates_preserve_order(items):
    """
    Remove duplicate items from a list while preserving order.
    
    Args:
        items: A list of items
        
    Returns:
        A new list with duplicates removed, order preserved
        
    Bug: Off-by-one error in the range - skips the last item!
    """
    seen = set()
    result = []
    
    # Bug: range(len(items) - 1) skips the last element!
    # Should be: range(len(items))
    for i in range(len(items) - 1):
        item = items[i]
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result


def calculate_moving_average(values, window_size):
    """
    Calculate moving average of a list with a given window size.
    
    Args:
        values: List of numeric values
        window_size: Size of the moving window
        
    Returns:
        List of moving averages
        
    Bug: Off-by-one error causes incorrect window calculation
    """
    if window_size <= 0 or window_size > len(values):
        raise ValueError("Invalid window size")
    
    averages = []
    
    # Bug: This should be range(len(values) - window_size + 1)
    # The current code either misses the last window or crashes
    for i in range(len(values) - window_size):
        window = values[i:i + window_size]
        avg = sum(window) / len(window)
        averages.append(avg)
    
    return averages


def extract_subsequence(sequence, start, end):
    """
    Extract a subsequence from a list using start and end indices.
    
    Args:
        sequence: The source list
        start: Start index (inclusive)
        end: End index (should be inclusive in this API)
        
    Returns:
        The subsequence from start to end (inclusive)
        
    Bug: Uses exclusive end index when API should use inclusive
    """
    # Bug: Off-by-one error - end index is exclusive but should be inclusive
    # Users expect extract_subsequence([1,2,3,4,5], 1, 3) to return [2, 3, 4]
    # But it returns [2, 3] due to Python's default exclusive end
    return sequence[start:end]
