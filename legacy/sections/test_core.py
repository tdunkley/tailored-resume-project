import logging

# ...existing code...

def test_core_functionality(core_data):
    """Test the core functionality."""
    assert 'key' in core_data, "Key is missing"
    logging.info("Core functionality test passed")

# ...existing code...
