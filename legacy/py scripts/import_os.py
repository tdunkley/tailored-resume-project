import os
import logging

# ...existing code...

def create_directory(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    logging.info(f"Directory created: {path}")

# ...existing code...
