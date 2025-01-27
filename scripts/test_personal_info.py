import json
from jinja2 import Template
import os

# Function to dynamically validate a section
def validate_section(section_name, section_data):
    validation_results = []

    # Ensure the section has data
    if not section_data:
        validation_results.append(f"Error: Section '{section_name}' is empty.")
        return validation_results

    # Validate content and formatting dynamically
    for key, value in section_data.items():
        if isinstance(value, dict) and "content" in value and "formatting" in value:
            validation_results.append(f"Validation Passed: Key '{key}' contains 'content' and 'formatting'.")
        else:
            validation_results.append(f"Warning: Key '{key}' is missing 'content' or 'formatting'.")

    return validation_results

# Function to generate inline HTML preview dynamically
def generate_html_preview(section_name, section_data, output_path):
    # Template for preview
    html_template = Template(
        """
        <html>
        <head><title>{{ section_name }} Preview</title></head>
        <body>
            <h2>{{ section_name | capitalize }}</h2>
            {% for key, value in section_data.items() %}
                <h3>{{ key | capitalize }}</h3>
                {% if value.content %}
                    <p><strong>Content:</strong> {{ value.content }}</p>
                {% endif %}
                {% if value.formatting %}
                    <p><strong>Formatting:</strong> {{ value.formatting }}</p>
                {% endif %}
            {% endfor %}
        </body>
        </html>
        """
    )

    # Render preview
    html_content = html_template.render(section_name=section_name, section_data=section_data)

    # Save HTML preview
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

# Main function to test a single section
def test_section(section_name, json_path, output_dir):
    # Load JSON
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if section_name not in data:
        print(f"Error: Section '{section_name}' not found in JSON.")
        return

    section_data = data[section_name]

    # Step 1: Validate section
    validation_results = validate_section(section_name, section_data)
    for result in validation_results:
        print(result)

    # Step 2: Generate inline HTML preview
    html_output_path = os.path.join(output_dir, f"{section_name}_preview.html")
    generate_html_preview(section_name, section_data, html_output_path)
    print(f"HTML Preview generated at: {html_output_path}")

# Entry point
if __name__ == "__main__":
    # Define paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    json_path = os.path.join(project_root, "data/resume.json")
    output_dir = os.path.join(project_root, "outputs")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Test personal information section
    test_section("personal_information", json_path, output_dir)



