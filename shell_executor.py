"""
shell_executor.py - Module with a security flaw: Command Injection

This module executes shell commands based on user input.
The bug: The function doesn't sanitize user input, allowing command injection attacks.
"""

import subprocess
import os


def execute_file_operation(operation, filename):
    """
    Execute a file operation (copy, delete, list) on a specified file.
    
    Args:
        operation: The operation to perform ('copy', 'delete', 'list')
        filename: The target filename (UNSANITIZED - SECURITY FLAW!)
        
    Returns:
        The output of the command as a string
        
    Security Issue: User input is directly interpolated into shell command.
                   An attacker could inject shell commands via filename parameter.
    """
    if operation == "copy":
        # Bug: filename is not sanitized, allows command injection
        cmd = f"copy {filename} {filename}.backup"
    elif operation == "delete":
        cmd = f"del {filename}"
    elif operation == "list":
        cmd = f"dir {filename}"
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    # Executing unsanitized user input in shell
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def get_file_info(filename):
    """
    Retrieve file information using shell command.
    
    Args:
        filename: The file to get info on (UNSANITIZED - SECURITY FLAW!)
        
    Returns:
        File information as a string
        
    Security Issue: Directly concatenates user input into shell command.
    """
    # Bug: Vulnerable to injection - user can pass "; rm -rf /" or similar
    cmd = f"powershell -Command \"Get-Item '{filename}' | Select-Object FullName, Length\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout
