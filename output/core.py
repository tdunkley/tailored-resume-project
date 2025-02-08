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
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )

def get_paths():
    """Get all critical paths for the project."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    paths = {
        "base_dir": base_dir,
        "scripts_dir": os.path.join(base_dir, "scripts"),
        "sections_dir": os.path.join(base_dir, "scripts", "sections"),
        "s3_operations_dir": os.path.join(base_dir, "scripts", "s3_operations"),
        "output_dir": os.path.join(base_dir, "output"),
        "resume_json": os.path.join(base_dir, "resume.json"),
    }
    for key, path in paths.items():
        logging.info(f"Path '{key}': {path}")
    return paths

def validate_paths(paths):
    """Ensure all critical paths exist and are accessible."""
    missing_paths = [f"{key}: {path}" for key, path in paths.items() if not os.path.exists(path) and key != "output_dir"]
    if missing_paths:
        logging.error("Validation failed for the following paths:")
        for missing in missing_paths:
            logging.error(f"Missing or inaccessible: {missing}")
        raise FileNotFoundError("One or more critical paths are missing or inaccessible.")
    logging.info("All paths validated successfully.")

def load_json(file_path):
    """Load JSON data from a file."""
    if not os.path.exists(file_path):
        logging.error(f"JSON file not found at {file_path}.")
        raise FileNotFoundError(f"JSON file not found at {file_path}.")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        logging.info(f"Data loaded successfully from {file_path}.")
        return data

if __name__ == "__main__":
    setup_logging()
    paths = get_paths()
    validate_paths(paths)
    resume_data = load_json(paths["resume_json"])
    logging.info(f"Resume data keys: {list(resume_data.keys())}")
