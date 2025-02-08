import logging
from docx import Document
import os
import json

def process_sections(section_name, resume_data, output_dir):
    """Process sections of the resume."""
    logger = logging.getLogger("section_processor")
    logger.info(f"Processing section: {section_name}")
    section_data = resume_data.get("sections", {}).get(section_name, {})
    output_path = os.path.join(output_dir, f"{section_name}.json")
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(section_data, json_file, indent=4)
    logger.info(f"Section {section_name} processed and saved to {output_path}")
