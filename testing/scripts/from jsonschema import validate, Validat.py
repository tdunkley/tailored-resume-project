import os
import json
from jsonschema import validate, ValidationError

# Print current working directory for debugging
print(f"Current working directory: {os.getcwd()}")

# Path to JSON file
file_path = "data/tailored_resume.json"

# Ensure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Validate JSON structure
with open(file_path, "r") as file:
    data = json.load(file)
    print("JSON data loaded successfully!")

# Example JSON schema validation (if schema is defined)
SCHEMA = {
    "type": "object",
    "properties": {
        "personal_information": {"type": "object"},
        "summary": {"type": "object"},
        "skills": {"type": "object"},
        "experience": {"type": "object"},
        "education": {"type": "object"},
    },
    "required": ["personal_information", "summary", "skills", "experience", "education"],
}

try:
    validate(instance=data, schema=SCHEMA)
    print("JSON is valid!")
except ValidationError as e:
    print(f"JSON validation error: {e}")
