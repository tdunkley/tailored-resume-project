import os
import sys
import logging
from key_mapper import map_keys
from validation_engine import validate_global_rules
from s3_manager import download_from_s3

def setup_paths():
    """Set up dynamic paths for imports."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    sys.path.append(project_root)
    sys.path.append(os.path.join(project_root, "scripts"))
    sys.path.append(os.path.join(project_root, "scripts", "sections"))
    sys.path.append(os.path.join(project_root, "scripts", "s3_operations"))

setup_paths()

def setup_header():
    """Set up and validate the header logic."""
    try:
        logging.info("Loading resume data...")
        # Attempt to load resume.json dynamically
        resume_data = download_from_s3("resume.json")
        logging.info("Resume data loaded successfully.")

        # Validate global rules
        validation_errors = validate_global_rules(resume_data)
        if validation_errors:
            raise ValueError(f"Validation Errors: {validation_errors}")

        # Example of using key mapping (optional)
        mapped_key = map_keys("personal_info", resume_data)
        logging.info(f"Mapped key for 'personal_info': {mapped_key}")

        return resume_data

    except Exception as e:
        logging.error(f"Error setting up header: {e}")
        raise
