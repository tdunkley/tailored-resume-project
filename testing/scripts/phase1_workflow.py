from docxtpl import DocxTemplate

# Test data
data = {
    "name": "Troy D. Dunkley",
    "desired_role": "Data Analytics Executive",
    "summary": "Visionary Data and Analytics Executive with over 15 years of experience.",
    "skills": "Python, SQL, Power BI, AWS",
    "experience": "Black Nisus, LLC: Data Evangelist (2020 - Present)",
    "education": "MBA, Keller Graduate School of Management",
    "key_achievements": "Improved efficiency by 30%.",
    "projects": "UA Archive: Improved data compliance and analytics."
}

TEMPLATE_PATH = "resume_template.docx"
OUTPUT_PATH = "rendered_resume.docx"

try:
    print("Loading the template...")
    template = DocxTemplate(TEMPLATE_PATH)

    print("Rendering the template with data...")
    template.render(data)

    print("Saving the rendered resume...")
    template.save(OUTPUT_PATH)
    print(f"Resume successfully saved to {OUTPUT_PATH}")
except Exception as e:
    print(f"An error occurred: {e}")
