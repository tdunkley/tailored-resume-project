import os
import logging
import json
import jsonschema
from jsonschema import validate
from pathlib import Path

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

def setup_logging(log_file, log_level):
    """Setup logging configuration."""
    logging.basicConfig(filename=log_file, level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    return logger

def get_paths():
    """Get paths from the configuration."""
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config['paths']

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
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def validate_json_schema(data, schema):
    """Validate JSON data against a schema."""
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise ValueError(f"JSON validation error: {e.message}")

if __name__ == "__main__":
    setup_logging("application.log", logging.INFO)
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
