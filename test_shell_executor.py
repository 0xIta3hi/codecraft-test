"""
test_shell_executor.py - Test suite for shell_executor.py

Tests file operation functions with security validation.
Tests WILL FAIL or expose vulnerabilities with the current buggy code.
"""

import pytest
import tempfile
import os
from pathlib import Path
from shell_executor import execute_file_operation, get_file_info


@pytest.fixture
def temp_file():
    """Create a temporary test file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("test content")
        temp_path = f.name
    yield temp_path
    # Cleanup
    if os.path.exists(temp_path):
        os.remove(temp_path)
    backup_path = f"{temp_path}.backup"
    if os.path.exists(backup_path):
        os.remove(backup_path)


def test_execute_file_operation_copy(temp_file):
    """Test that file copy operation works correctly."""
    result = execute_file_operation("copy", temp_file)
    # After copy, backup file should exist
    backup_path = f"{temp_file}.backup"
    assert os.path.exists(backup_path), "Backup file should be created"


def test_execute_file_operation_sanitized_input(temp_file):
    """Test that filenames with special characters are handled safely."""
    # This test validates that dangerous characters don't execute
    # With unsanitized input, this could execute arbitrary commands
    malicious_filename = f"{temp_file}' & echo 'INJECTION'"
    
    # Attempting injection should fail gracefully or be blocked
    with pytest.raises((FileNotFoundError, OSError)):
        execute_file_operation("copy", malicious_filename)


def test_get_file_info_requires_sanitization(temp_file):
    """Test that file info function properly sanitizes input."""
    # Current code is vulnerable to injection
    # Safe code should handle or reject special characters
    
    # This should work with legitimate filenames
    result = get_file_info(temp_file)
    assert len(result) > 0, "File info should be returned for valid file"
    
    # Test with injection attempt
    malicious_input = f"{temp_file}'; cmd /c calc; echo '"
    # Should either handle gracefully or raise an error
    with pytest.raises((FileNotFoundError, OSError, ValueError)):
        get_file_info(malicious_input)


def test_execute_file_operation_with_spaces_in_filename(temp_file):
    """Test that filenames with spaces are handled correctly."""
    # Create a file with spaces in the name
    spaces_file = temp_file.replace('.txt', ' with spaces.txt')
    with open(spaces_file, 'w') as f:
        f.write("test")
    
    try:
        # Should handle spaces correctly
        result = execute_file_operation("copy", spaces_file)
        assert os.path.exists(f"{spaces_file}.backup")
    finally:
        if os.path.exists(spaces_file):
            os.remove(spaces_file)
        if os.path.exists(f"{spaces_file}.backup"):
            os.remove(f"{spaces_file}.backup")
