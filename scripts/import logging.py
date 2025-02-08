import logging
from header import setup_header

def test_header():
    """Test the header logic."""
    try:
        logging.info("Testing dynamic header...")
        resume_data = setup_header()
        logging.info("Header setup and validation successful.")
        return resume_data
    except Exception as e:
        logging.error(f"Header test failed: {e}")
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    test_header()
