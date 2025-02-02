import os
import sys
import logging

# Dynamically add the path to the core module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from core import setup_logging, get_paths, validate_paths, load_resume_data

# Set up logging for the test
setup_logging()

try:
    # Step 1: Retrieve and validate paths
    logging.info("Testing core module...")
    paths = get_paths()
    validate_paths(paths)

    # Step 2: Load resume data
    logging.info("Testing resume data loading...")
    resume_data = load_resume_data(paths["resume_json"])

    # Step 3: Confirm keys exist in resume data
    logging.info("Validating loaded resume data keys...")
    assert "rules" in resume_data, "Key 'rules' not found in resume data."
    assert "sections" in resume_data, "Key 'sections' not found in resume data."

    logging.info("Core module test passed successfully!")

except Exception as e:
    logging.error(f"Core module test failed: {e}", exc_info=True)
