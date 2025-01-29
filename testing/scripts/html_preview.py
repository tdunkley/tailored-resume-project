import json

def generate_html_preview(json_data, output_path):
    html_content = "<html><head><style>"
    html_content += """
    body { font-family: Arial, sans-serif; line-height: 1.5; }
    h1 { font-size: 16pt; font-weight: bold; text-align: left; }
    h2 { font-size: 14pt; font-weight: bold; margin-top: 20px; }
    p { font-size: 12pt; }
    ul { margin: 10px 0; padding-left: 20px; }
    li { font-size: 12pt; }
    """
    html_content += "</style></head><body>"

    # Personal Information
    html_content += f"<h1>{json_data['personal_information']['name']}</h1>"
    html_content += f"<p><i>{json_data['personal_information']['desired_role']}</i></p>"

    # Summary
    html_content += "<h2>Summary</h2>"
    summary_data = json_data.get("summary", {})
    static_content = summary_data.get("static_content", "")
    dynamic_content = summary_data.get("dynamic_content", "")
    summary_text = f"{static_content} {dynamic_content}".strip()
    if not summary_text:
        summary_text = "Summary not available."
    html_content += f"<p>{summary_text}</p>"

    # Skills
    html_content += "<h2>Skills</h2>"
    skills = json_data.get("skills", {})
    if "groups" in skills:
        for group in skills["groups"]:
            html_content += f"<p><strong>{group['group_name']}</strong>: {', '.join(group['skills_list'])}</p>"
    else:
        html_content += "<p>Skills not available.</p>"

    # Experience
    html_content += "<h2>Experience</h2>"
    experience = json_data.get("experience", {}).get("roles", [])
    if experience:
        for role in experience:
            html_content += f"<h3>{role['title']} at {role['company']}</h3>"
            html_content += f"<p><i>{role['location']} | {role['dates']}</i></p>"
            html_content += "<ul>"
            for responsibility in role.get("responsibilities", []):
                html_content += f"<li>{responsibility}</li>"
            html_content += "</ul>"
    else:
        html_content += "<p>Experience not available.</p>"

    # Close HTML
    html_content += "</body></html>"

    # Write to output file
    with open(output_path, "w") as file:
        file.write(html_content)

# Load JSON data
json_path = "test_data/resume.json"
output_path = "output/preview.html"

with open(json_path, "r") as f:
    json_data = json.load(f)

# Generate HTML preview
generate_html_preview(json_data, output_path)
print(f"HTML preview has been generated at {output_path}")
