import json
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx import Document

# Helper: Replace Placeholder with Content and Apply Formatting
def replace_placeholder(doc, placeholder, content, formatting=None):
    for paragraph in doc.paragraphs:
        if placeholder in paragraph.text:
            paragraph.text = content
            if formatting:
                for run in paragraph.runs:
                    if "font_size" in formatting:
                        run.font.size = Pt(formatting["font_size"])
                    if "font_style" in formatting and formatting["font_style"] == "bold":
                        run.bold = True
            return

# Process Personal Information Section
def process_personal_information(doc, personal_data):
    replace_placeholder(
        doc,
        "{{name}}",
        personal_data["name"].upper(),
        formatting={"font_size": 14, "font_style": "bold"}
    )
    replace_placeholder(doc, "{{desired_role}}", personal_data["desired_role"])
    contact_info = (
        f"Phone: {personal_data['contact_info']['phone']} | "
        f"Email: {personal_data['contact_info']['email']} | "
        f"LinkedIn: {personal_data['contact_info']['linkedin']} | "
        f"Location: {personal_data['contact_info']['location']}"
    )
    replace_placeholder(doc, "{{contact_info}}", contact_info)

# Process Summary Section
def process_summary(doc, summary_data):
    content = f"{summary_data['static_content']} {summary_data['dynamic_content']}"
    replace_placeholder(doc, "{{summary}}", content)

# Process Skills Section
def process_skills(doc, skills_data):
    skills_content = "\n".join(
        f"{group['group_name']}: {', '.join(group['skills_list'])}"
        for group in skills_data["groups"]
    )
    replace_placeholder(doc, "{{skills}}", skills_content)

# Main Rendering Function
def render_resume(json_path, template_path, output_path):
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    doc = Document(template_path)

    process_personal_information(doc, data["personal_information"])  # Validated
    process_summary(doc, data["summary"])  # Revalidate formatting
    process_skills(doc, data["skills"])  # Revalidate formatting

    # Save the output
    doc.save(output_path)

# Paths
json_path = "test_data/resume.json"
template_path = "test_templates/resume_template.docx"
output_path = "output/final_resume_formatting_test.docx"

# Execute
render_resume(json_path, template_path, output_path)


