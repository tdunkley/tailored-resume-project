import logging

# ...existing code...

def test_header_functionality(header_data):
    """Test the header functionality."""
    assert 'title' in header_data, "Title is missing"
    logging.info("Header functionality test passed")

# ...existing code...
