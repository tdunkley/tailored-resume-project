import logging

# ...existing code...

def format_bullets(text):
    """Format text with bullet points."""
    return f"• {text}"

def format_spacing(text, before=1, after=1):
    """Format text with spacing."""
    return f"\n" * before + text + f"\n" * after

# ...existing code...
