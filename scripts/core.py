import os
import logging
import json

def setup_logging(log_filename="application.log"):
    """Set up logging for the application."""
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def get_paths():
    """
    Get all critical paths for the project.
    Returns:
        dict: Dictionary of paths.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    paths = {
        "base_dir": base_dir,
        "scripts_dir": os.path.join(base_dir, "scripts"),
        "sections_dir": os.path.join(base_dir, "scripts", "sections"),
        "s3_operations_dir": os.path.join(base_dir, "scripts", "s3_operations"),
        "output_dir": os.path.join(base_dir, "output"),
        "resume_json": os.path.join(base_dir, "resume.json"),
    }

    # Log paths for debugging purposes
    for key, path in paths.items():
        logging.info(f"Path '{key}': {path}")
    
    return paths

def validate_paths(paths):
    """
    Ensure all critical paths exist and are accessible.
    Args:
        paths (dict): Dictionary of paths to validate.
    """
    missing_paths = []
    for key, path in paths.items():
        if not os.path.exists(path) and key != "output_dir":  # Skip pre-check for output_dir
            missing_paths.append(f"{key}: {path}")
    
    if missing_paths:
        logging.error("Validation failed for the following paths:")
        for missing in missing_paths:
            logging.error(f"Missing or inaccessible: {missing}")
        raise FileNotFoundError("One or more critical paths are missing or inaccessible.")
    
    logging.info("All paths validated successfully.")

def load_resume_data(resume_json_path):
    """
    Load resume data from a local file.
    Args:
        resume_json_path (str): Path to the resume JSON file.
    Returns:
        dict: Resume data.
    """
    if not os.path.exists(resume_json_path):
        logging.error(f"Resume JSON file not found at {resume_json_path}.")
        raise FileNotFoundError(f"Resume JSON file not found at {resume_json_path}.")

    with open(resume_json_path, "r", encoding="utf-8") as file:
        resume_data = json.load(file)
        logging.info("Resume data loaded successfully.")
        return resume_data

if __name__ == "__main__":
    setup_logging()
    paths = get_paths()
    validate_paths(paths)
    resume_data = load_resume_data(paths["resume_json"])
    logging.info(f"Resume data keys: {list(resume_data.keys())}")
