#!/usr/bin/env python3
"""
Example Python module created by KaptainKube.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! This file was created via GitHub API."

def main():
    """Main function."""
    message = greet("World")
    print(message)

if __name__ == "__main__":
    main()
