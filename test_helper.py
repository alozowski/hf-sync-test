"""Helper functions for testing - should be tracked"""

def format_message(text: str) -> str:
    """Format a message with a prefix."""
    return f"[TEST] {text}"

def validate_input(value: str) -> bool:
    """Validate user input."""
    return len(value) > 0 and value.strip() != ""
