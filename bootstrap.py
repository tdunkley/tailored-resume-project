import os
import sys
import logging
import json
from datetime import datetime

# Dynamically add the scripts directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.join(current_dir, "scripts")
sys.path.append(scripts_dir)

from core import get_paths, setup_logging
from tracker import CentralizedTracker
from validation_engine import validate_global_rules, validate_cross_sectional_rules
from section_processor import process_sections

# Configure logging
setup_logging("bootstrap.log")
logger = logging.getLogger("bootstrap")
tracker = CentralizedTracker()

# Dependency validation
REQUIRED_FILES = [
    "config.json",
    "resume.json",
    "scripts/tracker.py",
    "scripts/section_processor.py",
    "scripts/validation_engine.py",
    "scripts/core.py"
]

REQUIRED_FUNCTIONS = {
    "tracker": ["CentralizedTracker"],
    "section_processor": ["process_sections"],
    "validation_engine": ["validate_global_rules", "validate_cross_sectional_rules"],
    "core": ["get_paths", "setup_logging"]
}

def validate_dependencies():
    """Validate that all required files and functions exist."""
    logger.info("Validating dependencies...")

    # Check for required files
    missing_files = [file for file in REQUIRED_FILES if not os.path.exists(os.path.join(current_dir, file))]
    if missing_files:
        logger.error(f"Missing files: {', '.join(missing_files)}")
        sys.exit(1)

    # Check for required functions
    missing_functions = []
    for module_name, functions in REQUIRED_FUNCTIONS.items():
        try:
            module = __import__(module_name)
            for func in functions:
                if not hasattr(module, func):
                    missing_functions.append(f"{func} in {module_name}")
        except ImportError as e:
            missing_functions.append(f"Module {module_name} could not be imported: {str(e)}")

    if missing_functions:
        logger.error(f"Missing functions or modules: {', '.join(missing_functions)}")
        sys.exit(1)

    logger.info("All dependencies validated successfully.")

def main():
    """Main bootstrap process."""
    try:
        tracker.start_tracking("Bootstrap Initialization")
        logger.info("Initializing bootstrap process...")

        # Validate dependencies
        validate_dependencies()

        # Retrieve paths
        paths = get_paths()

        # Load configuration
        tracker.start_tracking("Load Configuration")
        config_path = os.path.join(current_dir, "config.json")
        with open(config_path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
        tracker.end_tracking("Load Configuration")

        # Load resume data
        tracker.start_tracking("Load Resume Data")
        resume_path = paths["resume_json"]
        with open(resume_path, "r", encoding="utf-8") as resume_file:
            resume_data = json.load(resume_file)
        tracker.end_tracking("Load Resume Data")

        # Validate global and cross-sectional rules
        tracker.start_tracking("Validate Global Rules")
        validate_global_rules(resume_data)
        tracker.end_tracking("Validate Global Rules")

        tracker.start_tracking("Validate Cross-Sectional Rules")
        validate_cross_sectional_rules(resume_data)
        tracker.end_tracking("Validate Cross-Sectional Rules")

        # Process sections
        tracker.start_tracking("Process Sections")
        for section_name in resume_data.get("sections", {}).keys():
            process_sections(section_name, resume_data, tracker, paths)
        tracker.end_tracking("Process Sections")

        tracker.end_tracking("Bootstrap Initialization")
        logger.info("Bootstrap process completed successfully.")

    except Exception as e:
        tracker.track_error(f"Bootstrap Error: {e}")  # Correct the method call
        logger.error(f"An error occurred during the bootstrap process: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
