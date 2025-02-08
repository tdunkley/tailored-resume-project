import os
import json
import logging
from docx import Document
from sections import add_personal_information, add_skills_section, add_experience_section, add_education_section, add_certifications_section, add_key_achievements_section, add_projects_section, add_section_header, add_section_content
from validation import validate_resume_data

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def tailor_resume(resume_data, job_description):
    """Tailor the resume data based on the job description."""
    # Example tailoring: Add job title to the summary
    resume_data["sections"]["summary"].append(f"Applying for the role of {job_description['title']} at {job_description['companyName']}.")
    
    # Example tailoring: Add job-specific skills
    job_specific_skills = job_description.get("requirements", "").split(", ")
    for skill in job_specific_skills:
        if skill and skill not in resume_data["sections"]["skills"]["groups"][0]["skills_list"]:
            resume_data["sections"]["skills"]["groups"][0]["skills_list"].append(skill)
    
    # Additional tailoring logic can be added here

def apply_formatting(run, formatting):
    """Apply formatting to a run."""
    run.font.name = formatting.get("font", "Arial")
    run.font.size = Pt(formatting.get("size", 10))
    run.font.bold = formatting.get("bold", False)
    run.font.color.rgb = RGBColor.from_string(formatting.get("color", "#000000").replace("#", ""))

def generate_resume(resume_data, config, job_description, output_filename):
    """Generate a resume Word document based on the resume data, job description, and config."""
    document = Document()

    # Tailor the resume data based on the job description
    tailor_resume(resume_data, job_description)

    # Validate resume data
    validate_resume_data(resume_data, config)

    # Add Personal Information section without a section header
    add_personal_information(document, resume_data["sections"]["personal_information"], config["formatting"])

    # Add Summary section
    add_section_header(document, "Summary", config["formatting"])
    add_section_content(document, resume_data["sections"]["summary"], config["formatting"])

    # Add Skills section
    add_skills_section(document, resume_data["sections"]["skills"], config["formatting"])

    # Add Experience section
    add_experience_section(document, resume_data["sections"]["experience"], config["formatting"])

    # Add Education section
    add_education_section(document, resume_data["sections"]["education"], config["formatting"])

    # Add Certifications section
    add_certifications_section(document, resume_data["sections"]["certifications"], config["formatting"])

    # Add Key Achievements section
    add_key_achievements_section(document, resume_data["sections"]["key_achievements"], config["formatting"])

    # Add Projects section
    add_projects_section(document, resume_data["sections"]["projects"], config["formatting"])

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the document
    document.save(output_filename)
    logging.info(f"Resume generated and saved to {output_filename}")

if __name__ == "__main__":
    # Load configuration
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, 'r') as file:
        config = json.load(file)

    # Load tailored resume data
    resume_path = os.path.join(os.path.dirname(__file__), "resume_tdunkley.json")
    with open(resume_path, 'r') as file:
        resume_data = json.load(file)

    # Load job descriptions from Huntr Wishlist
    job_descriptions_path = os.path.join(os.path.dirname(__file__), "huntr_job_descriptions.json")
    with open(job_descriptions_path, 'r') as file:
        job_descriptions = json.load(file)

    # Filter job descriptions and generate resumes
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for job_description in job_descriptions:
        if not job_description.get("description"):
            logging.info(f"Skipping job description with empty details: {job_description}")
            continue

        output_filename = os.path.join(output_dir, f"resume_{job_description['companyName'].replace(' ', '_').lower()}_{job_description['title'].replace(' ', '_').lower()}.docx")
        generate_resume(resume_data, config, job_description, output_filename)

# Debug statement to confirm the file is being executed
print("resume_generator.py loaded successfully")
