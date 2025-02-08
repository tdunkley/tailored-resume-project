from docx import Document
import json
import os

def extract_resume_data(doc_path):
    """Extract data from a Word document and convert it to JSON format."""
    document = Document(doc_path)
    resume_data = {
        "sections": {
            "personal_information": {},
            "summary": {},
            "skills": {"groups": []},
            "experience": {"roles": []},
            "education": {"entries": []},
            "key_achievements": {"entries": []},
            "projects": {"entries": []}
        }
    }

    current_section = None
    for para in document.paragraphs:
        text = para.text.strip()
        if text:
            if text.upper() in resume_data["sections"]:
                current_section = text.lower().replace(" ", "_")
            elif current_section:
                if current_section == "personal_information":
                    if "name" not in resume_data["sections"][current_section]:
                        resume_data["sections"][current_section]["name"] = text
                    else:
                        resume_data["sections"][current_section]["contact_info"] = text
                elif current_section == "summary":
                    resume_data["sections"][current_section]["static_content"] = text
                elif current_section == "skills":
                    resume_data["sections"][current_section]["groups"].append({"group_name": "Skills", "skills_list": text.split(", ")})
                elif current_section == "experience":
                    if "roles" not in resume_data["sections"][current_section]:
                        resume_data["sections"][current_section]["roles"] = []
                    resume_data["sections"][current_section]["roles"].append({"responsibilities": text.split(", ")})
                elif current_section == "education":
                    resume_data["sections"][current_section]["entries"].append({"school": text})
                elif current_section == "key_achievements":
                    resume_data["sections"][current_section]["entries"].append({"title": text})
                elif current_section == "projects":
                    resume_data["sections"][current_section]["entries"].append({"title": text})

    return resume_data

def save_resume_data(resume_data, output_file):
    """Save resume data to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(resume_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    doc_path = "path/to/your/resume.docx"  # Replace with the path to your Word document
    output_file = "resume.json"

    try:
        resume_data = extract_resume_data(doc_path)
        save_resume_data(resume_data, output_file)
        print(f"Resume data saved to {output_file}")
    except Exception as e:
        print(f"Error processing resume document: {e}")
