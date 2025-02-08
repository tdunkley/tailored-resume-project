import logging

# ...existing code...

def test_personal_info(personal_info):
    """Test the personal information section."""
    assert 'name' in personal_info, "Name is missing"
    assert 'contact_info' in personal_info, "Contact info is missing"
    logging.info("Personal information test passed")

# ...existing code...
