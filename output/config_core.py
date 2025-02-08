import os
import logging
import json
import jsonschema
from jsonschema import validate

# Define the root directory dynamically
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths relative to the root directory
RESUME_FILE = os.path.join(ROOT_DIR, 'resume.json')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')

# Validate paths
if not os.path.exists(RESUME_FILE):
    raise FileNotFoundError(f"Resume file not found at {RESUME_FILE}")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Print paths for debugging
print(f"ROOT_DIR: {ROOT_DIR}")
print(f"RESUME_FILE: {RESUME_FILE}")
print(f"OUTPUT_DIR: {OUTPUT_DIR}")

def setup_logging(log_filename="application.log"):
    """Set up logging for the application."""
    log_dir = os.path.join(ROOT_DIR, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, log_filename)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )

def get_paths():
    """Get all critical paths for the project."""
    paths = {
        "base_dir": ROOT_DIR,
        "scripts_dir": os.path.join(ROOT_DIR, "scripts"),
        "sections_dir": os.path.join(ROOT_DIR, "scripts", "sections"),
        "s3_operations_dir": os.path.join(ROOT_DIR, "scripts", "s3_operations"),
        "output_dir": OUTPUT_DIR,
        "resume_json": RESUME_FILE,
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

def validate_json_schema(data, schema):
    """Validate JSON data against a schema."""
    try:
        validate(instance=data, schema=schema)
        logging.info("JSON schema validation passed.")
    except jsonschema.exceptions.ValidationError as err:
        logging.error(f"JSON schema validation error: {err}")
        raise

if __name__ == "__main__":
    setup_logging()
    paths = get_paths()
    validate_paths(paths)
    resume_data = load_json(paths["resume_json"])
    logging.info(f"Resume data keys: {list(resume_data.keys())}")

    # Example schema validation (define your schema as needed)
    resume_schema = {
        "type": "object",
        "properties": {
            "sections": {"type": "object"},
            # Add more schema definitions as needed
        },
        "required": ["sections"]
    }
    validate_json_schema(resume_data, resume_schema)
