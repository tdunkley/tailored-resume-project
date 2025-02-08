from s3_manager import download_from_s3

def test_validation():
    # Load resume data once
    resume_data = download_from_s3("resume.json")

    # Sample content to validate
    content = {
        "name": "John Doe",
        "desired_role": "Senior Data Architect",
        "contact_info": {
            "phone": "+1-770-401-6527",
            "email": "john.doe@example.com",
            "location": "Atlanta, GA",
            "linkedin": "https://linkedin.com/in/johndoe"
        }
    }

    # Validate the personal_information section
    errors = validate_section("personal_information", content, resume_data)
    if errors:
        print("Validation Errors:", errors)
    else:
        print("Validation Passed")

if __name__ == "__main__":
    test_validation()
