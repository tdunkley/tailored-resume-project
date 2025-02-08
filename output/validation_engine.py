import json

def validate_global_rules(resume_data, config):
    """Validate global rules (e.g., mandatory sections)."""
    mandatory_sections = config["validation"]["global_rules"]["mandatory_sections"]
    missing_sections = [section for section in mandatory_sections if section not in resume_data["sections"]]
    return [f"Missing mandatory sections: {', '.join(missing_sections)}"] if missing_sections else []

def validate_sectional_rules(section_name, section_data, config):
    """Validate rules specific to a section."""
    errors = []
    if not section_data:
        return [f"Section '{section_name}' is empty or missing."]

    section_rules = config["validation"]["sectional_rules"].get(section_name, {})
    if section_name == "personal_information":
        if not section_data.get("name"):
            errors.append("Name is missing in personal information.")
        if not section_data.get("contact_info"):
            errors.append("Contact info is missing in personal information.")
        if section_rules.get("name_title_case") and not section_data["name"].istitle():
            errors.append("Name must be in title case.")

    # Add more rules for other sections here...

    return errors

def validate_cross_sectional_rules(resume_data, config):
    """Validate rules that span multiple sections."""
    sections_to_check = config["validation"]["cross_sectional_rules"]["no_duplicate_verbs"]["sections_to_check"]
    experience_verbs = extract_verbs_from_section(resume_data, "experience")
    key_achievement_verbs = extract_verbs_from_section(resume_data, "key_achievements")
    duplicate_verbs = set(experience_verbs) & set(key_achievement_verbs)
    return [f"Duplicate verbs across sections: {', '.join(duplicate_verbs)}"] if duplicate_verbs else []

def extract_verbs_from_section(resume_data, section_name):
    """Helper function to extract verbs from a section."""
    section = resume_data["sections"].get(section_name, {})
    verbs = [responsibility.split()[0].lower() for role in section.get("roles", []) for responsibility in role.get("responsibilities", [])]
    return verbs

def validate_resume(resume_data, config):
    """Run all validations and return errors."""
    errors = validate_global_rules(resume_data, config)
    for section_name, section_data in resume_data["sections"].items():
        errors.extend(validate_sectional_rules(section_name, section_data, config))
    errors.extend(validate_cross_sectional_rules(resume_data, config))
    return errors
