import os
import sys
import logging
from core import get_paths, load_resume_data, setup_logging
from validation_engine import validate_sectional_rules

# Dynamically add the core module path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(current_dir, "..")))

# Logging setup
setup_logging("personal_info.log")
logger = logging.getLogger("personal_info_section")

try:
    # Retrieving paths
    logger.info("Retrieving paths...")
    paths = get_paths()

    # Loading resume data
    logger.info("Loading resume data...")
    resume_data = load_resume_data(paths["resume_json"])

    # Extracting personal info section
    logger.info("Extracting personal information...")
    personal_info = resume_data.get("sections", {}).get("personal_information", {})
    if not personal_info:
        raise ValueError("Personal Information section is missing in the JSON file.")

    # Validating personal info
    logger.info("Validating personal information...")
    validation_errors = validate_sectional_rules("personal_information", personal_info)
    if validation_errors:
        raise ValueError(f"Validation errors in Personal Info: {validation_errors}")

    # Formatting personal information
    logger.info("Formatting personal information...")
    name = personal_info.get("name", "N/A")
    role = personal_info.get("desired_role", "N/A")
    contact = personal_info.get("contact_info", {})
    formatted_contact = " | ".join([
        f"+{contact.get('phone', 'N/A')}",
        f"email: {contact.get('email', 'N/A')}",
        f"location: {contact.get('location', 'N/A')}",
        f"linkedin: {contact.get('linkedin', 'N/A')}"
    ])

    formatted_output = f"{name}\n{role}\n{formatted_contact}"

    # Writing to output
    output_file = os.path.join(paths["output_dir"], "personal_info.txt")
    logger.info(f"Writing personal info to {output_file}...")
    os.makedirs(paths["output_dir"], exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted_output)

    logger.info("Personal information section written successfully.")

except Exception as e:
    logger.error(f"An error occurred in personal_info.py: {e}", exc_info=True)
