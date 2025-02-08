from docx import Document
import os

def process_sections(section_name, resume_data, output_dir):
    section_data = resume_data.get(section_name)
    if not section_data:
        print(f"Error: Section '{section_name}' not found.")
        return False

    print(f"Inline Preview for Section '{section_name}':")
    for key, value in section_data.items():
        print(f"{key}: {value}")
    print("-" * 50)

    # Create a new document from scratch
    document = Document()
    document.add_heading(section_name.upper(), level=1)
    for key, value in section_data.items():
        document.add_heading(key, level=2)
        document.add_paragraph(str(value))

    output_file = os.path.join(output_dir, f"{section_name}.docx")
    document.save(output_file)
    print(f"Document saved to {output_file}")
    return True
