import json
import os
import logging
import re

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("tailor_resume")

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    """Save JSON data to a file."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def tailor_resume(resume_data, job_description):
    """Tailor the resume data based on the job description."""
    logger.info("Tailoring resume based on job description...")
    
    # Example tailoring: Add job description to the summary section
    tailored_resume = resume_data.copy()
    tailored_resume["sections"]["summary"].append(f"Tailored for the role of {job_description['title']} at {job_description['companyName']}.")
    
    # Example tailoring: Highlight relevant skills
    job_keywords = job_description["description"].lower().split()
    for group in tailored_resume["sections"]["skills"]["groups"]:
        group["skills_list"] = [skill for skill in group["skills_list"] if any(keyword in skill.lower() for keyword in job_keywords)]
    
    # Example tailoring: Add job description to the resume
    tailored_resume["sections"]["job_description"] = job_description
    
    return tailored_resume

def sanitize_filename(filename):
    """Sanitize the filename by removing invalid characters."""
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def main():
    base_dir = os.path.normpath(r"C:\Users\troy_\Downloads\Tailored Resume Process\S3")
    resume_path = os.path.join(base_dir, "resume_tdunkley.json")
    job_descriptions_path = os.path.join(base_dir, "huntr_job_descriptions.json")
    output_dir = os.path.join(base_dir, "output")

    resume_data = load_json(resume_path)
    job_descriptions = load_json(job_descriptions_path)

    for job_description in job_descriptions:
        tailored_resume = tailor_resume(resume_data, job_description)
        sanitized_company_name = sanitize_filename(job_description['companyName'].replace(' ', '_').lower())
        sanitized_job_title = sanitize_filename(job_description['title'].replace(' ', '_').lower())
        resume_name = f"resume_{sanitized_company_name}_{sanitized_job_title}.json"
        output_path = os.path.join(output_dir, resume_name)
        save_json(tailored_resume, output_path)
        logger.info(f"Tailored resume saved to {output_path}")

if __name__ == "__main__":
    main()
