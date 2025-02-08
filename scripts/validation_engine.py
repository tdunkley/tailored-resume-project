<<<<<<< HEAD
import logging
import jsonschema
from jsonschema import validate

logger = logging.getLogger("validation_engine")

def validate_json_schema(data, schema):
    """Validate JSON data against a schema."""
    try:
        validate(instance=data, schema=schema)
        logger.info("JSON schema validation passed.")
    except jsonschema.exceptions.ValidationError as err:
        logger.error(f"JSON schema validation error: {err}")
        raise

def validate_global_rules(resume_data, config):
    """Validate global rules for the resume."""
    logger.info("Validating global rules")
    # Validate global rules as needed
    # ...

def validate_cross_sectional_rules(resume_data, config):
    """Validate cross-sectional rules for the resume."""
    logger.info("Validating cross-sectional rules")
    # Validate cross-sectional rules as needed
    # ...

def validate_sectional_rules(data, rules):
    """Validate sectional rules."""
    # Implement sectional validation logic
    pass

def run_validation(data, config):
    """Run all validation checks."""
    try:
        validate_json_schema(data, config["resume_schema"])
        validate_global_rules(data, config["validation"]["global_rules"])
        validate_cross_sectional_rules(data, config["validation"]["cross_sectional_rules"])
        validate_sectional_rules(data, config["validation"]["sectional_rules"])
        logger.info("All validation checks passed.")
    except Exception as e:
        logger.error(f"Validation error: {e}", exc_info=True)
        raise
=======
import json

def validate_global_rules(resume_data):
    """Validate global rules (e.g., mandatory sections)."""
    mandatory_sections = ["personal_information", "experience", "skills"]
    missing_sections = [section for section in mandatory_sections if section not in resume_data["sections"]]
    if missing_sections:
        return [f"Missing mandatory sections: {', '.join(missing_sections)}"]
    return []

def validate_sectional_rules(section_name, section_data):
    """Validate rules specific to a section."""
    errors = []
    if not section_data:
        errors.append(f"Section '{section_name}' is empty or missing.")
        return errors

    # Example validation for personal_information
    if section_name == "personal_information":
        if not section_data.get("name"):
            errors.append("Name is missing in personal information.")
        if not section_data.get("contact_info"):
            errors.append("Contact info is missing in personal information.")
        if not section_data["name"].istitle():
            errors.append("Name must be in title case.")

    # Add more rules for other sections here...

    return errors

def validate_cross_sectional_rules(resume_data):
    """Validate rules that span multiple sections."""
    errors = []
    # Example: Check for duplicate verbs across experience and key achievements
    experience_verbs = extract_verbs_from_section(resume_data, "experience")
    key_achievement_verbs = extract_verbs_from_section(resume_data, "key_achievements")
    duplicate_verbs = set(experience_verbs) & set(key_achievement_verbs)
    if duplicate_verbs:
        errors.append(f"Duplicate verbs across sections: {', '.join(duplicate_verbs)}")

    return errors

def extract_verbs_from_section(resume_data, section_name):
    """Helper function to extract verbs from a section."""
    section = resume_data["sections"].get(section_name, {})
    verbs = []
    if "roles" in section:
        for role in section["roles"]:
            for responsibility in role.get("responsibilities", []):
                verbs.append(responsibility.split()[0].lower())  # Extract first word as verb
    return verbs

def validate_resume(resume_data):
    """Run all validations and return errors."""
    errors = []
    errors.extend(validate_global_rules(resume_data))
    for section_name, section_data in resume_data["sections"].items():
        errors.extend(validate_sectional_rules(section_name, section_data))
    errors.extend(validate_cross_sectional_rules(resume_data))
    return errors
>>>>>>> 011eb20403b89d07c8ae11e5b4bc3094a262060f
