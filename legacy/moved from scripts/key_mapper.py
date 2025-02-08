import logging

# ...existing code...

def map_keys(data, key_mapping):
    """Map keys in the data based on the key mapping."""
    mapped_data = {}
    for old_key, new_key in key_mapping.items():
        if old_key in data:
            mapped_data[new_key] = data[old_key]
    logging.info(f"Keys mapped: {key_mapping}")
    return mapped_data

# ...existing code...
