import json
import logging

# ...existing code...

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    logging.info(f"Loaded JSON data from {file_path}")
    return data

# ...existing code...
