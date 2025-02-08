import logging
import json
import os
from docx import Document

# Define a mapping between DOCX section headers and JSON section headers
SECTION_HEADER_MAPPING = {
    "Personal Information": "personal_information",
    "Summary": "summary",
    "Skills": "skills",
    "Experience": "experience",
    "Education": "education",
    "Key Achievements": "key_achievements",
    "Projects": "projects",
    "Certifications": "certifications",
    "Certifications & Development": "certifications_and_development"
}

def is_section_header(paragraph):
    """Determine if a paragraph is a section header based on formatting or keywords."""
    if any(keyword in paragraph.text for keyword in SECTION_HEADER_MAPPING.keys()):
        return True
    if paragraph.style.name.startswith('Heading'):
        return True
    if paragraph.runs and paragraph.runs[0].bold:
        return True
    return False

def clean_section_header(header):
    """Clean up the section header to remove special characters and line breaks."""
    return header.replace("\n", " ").replace(":", "").strip().lower().replace(" ", "_")

def extract_resume_data(doc_path):
    """Extract data from the resume document."""
    logger = logging.getLogger("resume_parser")
    try:
        logger.info(f"Opening document: {doc_path}")
        document = Document(doc_path)
        resume_data = {"sections": {}}
        
        current_section = None
        for paragraph in document.paragraphs:
            text = paragraph.text.strip()
            logger.info(f"Paragraph text: {text}")
            
            if not text:
                continue
            
            if is_section_header(paragraph):
                # Map the section header to the corresponding JSON key
                cleaned_header = clean_section_header(text)
                current_section = SECTION_HEADER_MAPPING.get(text, cleaned_header)
                if current_section not in resume_data["sections"]:
                    resume_data["sections"][current_section] = []
                logger.info(f"Identified section: {current_section}")
            else:
                # Add content to the current section
                if current_section:
                    if current_section == "personal_information":
                        if "Name:" in text:
                            resume_data["sections"][current_section]["name"] = text.split("Name:")[1].strip()
                        elif "Desired Role:" in text:
                            resume_data["sections"][current_section]["desired_role"] = text.split("Desired Role:")[1].strip()
                        elif "Contact Info:" in text:
                            contact_info = text.split("Contact Info:")[1].strip().split(", ")
                            resume_data["sections"][current_section]["phone"] = contact_info[0]
                            resume_data["sections"][current_section]["email"] = contact_info[1]
                            resume_data["sections"][current_section]["linkedin"] = contact_info[2]
                            resume_data["sections"][current_section]["location"] = contact_info[3]
                    elif current_section == "experience":
                        # Handle experience section with commas and dashes
                        if "," in text:
                            parts = text.split(",")
                            if len(parts) == 3:
                                company, location, dates = parts
                                resume_data["sections"][current_section].append({
                                    "company": company.strip(),
                                    "location": location.strip(),
                                    "dates": dates.strip(),
                                    "responsibilities": []
                                })
                            else:
                                resume_data["sections"][current_section][-1]["responsibilities"].append(text.strip())
                        else:
                            resume_data["sections"][current_section][-1]["responsibilities"].append(text.strip())
                    else:
                        resume_data["sections"][current_section].append(text)
    
        logger.info(f"Extracted resume data: {json.dumps(resume_data, indent=4)}")
        return resume_data
    except Exception as e:
        logger.error(f"Error extracting resume data: {e}", exc_info=True)
        raise

def save_resume_data(resume_data, file_path):
    """Save resume data to a JSON file."""
    try:
        if not file_path:
            raise ValueError("File path is empty.")
        
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(resume_data, json_file, indent=4)
        logging.info(f"Resume data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving resume data: {e}", exc_info=True)
        raise
