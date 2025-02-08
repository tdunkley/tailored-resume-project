import os
import sys
import json

# Ensure the script can access shared modules
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.abspath(os.path.join(current_dir))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

try:
    from s3_operations.load_resume_from_s3 import load_resume_data_from_s3
except ImportError as e:
    raise ImportError(f"Error importing shared module: {e}")


def load_resume_data():
    """
    Load the resume JSON file, either from local storage or S3.
    """
    try:
        local_path = os.path.join(scripts_dir, "resume.json")
        if os.path.exists(local_path):
            print(f"Loading JSON from local file: {local_path}")
            with open(local_path, "r") as file:
                return json.load(file)
        else:
            print("Local file not found. Attempting to load from S3...")
            return load_resume_data_from_s3(
                bucket_name="resume-tailoring-storage", object_key="resume.json"
            )
    except Exception as e:
        raise FileNotFoundError(f"Failed to load resume.json: {e}")


def map_keys(section_name, resume_data):
    """
    Maps the given section name to its corresponding key in the JSON data.
    Returns the mapped key as a string.
    """
    key_mappings = {
        "personal_info": "personal_information",
        "summary": "summary",
        "skills": "skills",
        "experience": "experience",
        "education": "education",
        "key_achievements": "key_achievements",
        "projects": "projects"
    }

    # Ensure the section name exists in the mapping
    if section_name not in key_mappings:
        raise KeyError(f"Mapping for section '{section_name}' not found.")

    mapped_key = key_mappings[section_name]

    # Verify the mapped key exists in the resume_data
    if mapped_key not in resume_data.get("sections", {}):
        raise KeyError(f"'{mapped_key}' is missing in the JSON data.")

    return mapped_key


if __name__ == "__main__":
    # Test key mapping
    try:
        resume_data = load_resume_data()
        test_key = "personal_info"
        mapped_section = map_keys(test_key, resume_data)
        print(f"Mapped key for '{test_key}': {mapped_section}")
    except Exception as e:
        print(f"Error: {e}")
