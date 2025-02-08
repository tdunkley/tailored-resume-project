import json
from docx import Document

# Helper: Replace Placeholder with Content
def replace_placeholder(doc, placeholder, content):
    for paragraph in doc.paragraphs:
        if placeholder in paragraph.text:
            paragraph.text = content
            return

# Process Personal Information Section
def process_personal_information(doc, personal_data):
    replace_placeholder(doc, "{{name}}", personal_data["name"].upper())
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

# Process Experience Section
def process_experience(doc, experience_data):
    experience_content = "\n\n".join(
        f"{role['title']} - {role['company']} ({role['dates']})\n"
        f"{role['location']}\n"
        + "\n".join(f"- {resp}" for resp in role['responsibilities'])
        for role in experience_data["roles"]
    )
    replace_placeholder(doc, "{{experience_bullets}}", experience_content)

# Process Education Section
def process_education(doc, education_data):
    education_content = "\n\n".join(
        f"{entry['degree']}, {entry['focus']}\n{entry['school']}"
        for entry in education_data["entries"]
    )
    replace_placeholder(doc, "{{education}}", education_content)

# Process Key Achievements Section
def process_key_achievements(doc, achievements_data):
    achievements_content = "\n\n".join(
        f"{entry['title']}\n- {entry['description']}"
        for entry in achievements_data["entries"]
    )
    replace_placeholder(doc, "{{key_achievements}}", achievements_content)

# Process Projects Section
def process_projects(doc, projects_data):
    projects_content = "\n\n".join(
        f"{project['title']} - {project['company']} ({project['dates']})\n"
        f"Goal: {project['goal']}\n"
        f"Responsibilities: {project['responsibilities']}\n"
        f"Results: {project['results']}"
        for project in projects_data["entries"]
    )
    replace_placeholder(doc, "{{projects}}", projects_content)

# Main Rendering Function
def render_resume(json_path, template_path, output_path):
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    doc = Document(template_path)

    process_personal_information(doc, data["personal_information"])
    process_summary(doc, data["summary"])
    process_skills(doc, data["skills"])
    process_experience(doc, data["experience"])
    process_education(doc, data["education"])
    process_key_achievements(doc, data["key_achievements"])
    process_projects(doc, data["projects"])

    doc.save(output_path)

# Paths
json_path = "test_data/resume.json"
template_path = "test_templates/resume_template.docx"
output_path = "output/final_resume.docx"

# Execute
render_resume(json_path, template_path, output_path)
















