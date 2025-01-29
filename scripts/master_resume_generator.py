import sys
import os
import json
from docx import Document
from docxcompose.composer import Composer

# Add the correct scripts folder to the system path
#scripts_path = r"C:\Users\troy_\Downloads\Tailored Resume Process\resume_project\scripts"
#sys.path.append(scripts_path)

script_dir = os.path.dirname(os.path.realpath(__file__))
resume_path = os.path.join(script_dir, '..', 'resume.json')  # Navigates up one directory
with open(resume_path, 'r') as f:
    resume = json.load(f)

# Import your modules
from personal_info import generate_personal_info_section
from summary import generate_summary_section
from skills import generate_skills_section
from experience import generate_experience_section
from education import generate_education_section
from key_achievements import generate_key_achievements_section
from projects import generate_projects_section

def generate_full_resume():
    # Define output paths
    output_dir = r"C:\Users\troy_\Downloads\Tailored Resume Process\resume_project\output"
    final_resume = os.path.join(output_dir, "final_resume.docx")
    
    # Generate individual sections
    sections = {
        "personal_info": "personal_info_section.docx",
        "summary": "summary_section.docx",
        "skills": "skills_section.docx",
        "experience": "experience_section.docx",
        "education": "education_section.docx",
        "key_achievements": "key_achievements_section.docx",
        "projects": "projects_section.docx"
    }
    
    # Generate each section
    for section, filename in sections.items():
        section_path = os.path.join(output_dir, filename)
        globals()[f"generate_{section}_section"](section_path)
    
    # Combine all sections using docxcompose
    master = Document(os.path.join(output_dir, "personal_info_section.docx"))
    composer = Composer(master)
    
    # Add remaining sections in order
    for filename in list(sections.values())[1:]:
        doc = Document(os.path.join(output_dir, filename))
        composer.append(doc)
    
    # Save final resume
    composer.save(final_resume)
    print(f"Final resume generated at: {final_resume}")

if __name__ == "__main__":
    generate_full_resume()
