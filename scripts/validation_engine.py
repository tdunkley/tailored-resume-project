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
