import logging
from docx import Document
import json
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("section_parser")

# Define a mapping between DOCX section headers and JSON section headers
SECTION_HEADER_MAPPING = {
    "Summary": "summary",
    "Skills": "skills",
    "Experience": "experience",
    "Education": "education",
    "Key Achievements": "key_achievements",
    "Projects": "projects",
    "Certifications": "certifications",
    "Certifications & Development": "certifications_and_development"  # Add the new section here
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
    logger.info(f"Opening document: {doc_path}")
    document = Document(doc_path)
    resume_data = {"sections": {"personal_information": {}}}
    
    current_section = "personal_information"
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        logger.info(f"Paragraph text: {text}")
        
        if not text:
            continue
        
        if is_section_header(paragraph):
            # Map the section header to the corresponding JSON key
            cleaned_header = clean_section_header(text)
            current_section = SECTION_HEADER_MAPPING.get(text, cleaned_header)
            resume_data["sections"][current_section] = []
            logger.info(f"Identified section: {current_section}")
        else:
            # Add content to the current section
            if current_section == "personal_information":
                if "Name:" in text:
                    resume_data["sections"][current_section]["name"] = text.split("Name:")[1].strip()
                    logger.info(f"Added name to {current_section}: {resume_data['sections'][current_section]['name']}")
                elif "Desired Role:" in text:
                    resume_data["sections"][current_section]["desired_role"] = text.split("Desired Role:")[1].strip()
                    logger.info(f"Added desired role to {current_section}: {resume_data['sections'][current_section]['desired_role']}")
                elif "Contact Info:" in text:
                    contact_info = text.split("Contact Info:")[1].strip().split(", ")
                    resume_data["sections"][current_section]["phone"] = contact_info[0]
                    resume_data["sections"][current_section]["email"] = contact_info[1]
                    resume_data["sections"][current_section]["linkedin"] = contact_info[2]
                    resume_data["sections"][current_section]["location"] = contact_info[3]
                    logger.info(f"Added contact info to {current_section}: {resume_data['sections'][current_section]}")
            else:
                logger.info(f"Adding content to section {current_section}: {text}")
                resume_data["sections"][current_section].append(text)
    
    logger.info(f"Extracted resume data: {json.dumps(resume_data, indent=4)}")
    return resume_data

def main():
    """Main function to test section parsing."""
    doc_path = "c:/Users/troy_/Downloads/Tailored Resume Process/S3/full_cv.docx"  # Replace with the actual path to your Word document
    output_path = "c:/Users/troy_/Downloads/Tailored Resume Process/S3/full_cv.json"  # Ensure the file name is consistent
    try:
        logger.info("Starting resume extraction process...")
        resume_data = extract_resume_data(doc_path)
        
        # Verify the presence and content of each section
        for section, content in resume_data["sections"].items():
            logger.info(f"Section: {section}, Content: {content}")
            print(f"Section: {section}, Content: {content}")
        
        # Save the extracted data to a JSON file
        logger.info(f"Saving resume data to {output_path}")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(resume_data, f, indent=4)
        logger.info(f"Resume data saved to {output_path}")
        print(f"Resume data saved to {output_path}")
    except Exception as e:
        logger.error(f"Error during section parsing: {e}", exc_info=True)
        print(f"Error during section parsing: {e}")

if __name__ == "__main__":
    main()
