import os
import sys
import logging

# Setup dynamic paths
def setup_paths():
    """Set up dynamic paths for imports."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    sys.path.append(project_root)
    sys.path.append(os.path.join(project_root, "scripts"))
    sys.path.append(os.path.join(project_root, "scripts", "sections"))
    sys.path.append(os.path.join(project_root, "scripts", "s3_operations"))

setup_paths()

# Import required modules after paths are set
try:
    from key_mapper import map_keys
    from validation_engine import validate_global_rules
    from s3_manager import download_from_s3
except ImportError as e:
    logging.error(f"Failed to import a required module: {e}")
    raise

# Test the header setup
def test_header():
    """Test the header logic."""
    try:
        logging.info("Testing dynamic header...")
        from header import setup_header
        resume_data = setup_header()
        logging.info("Header setup and validation successful.")
        return resume_data
    except Exception as e:
        logging.error(f"Header test failed: {e}")
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    test_header()

