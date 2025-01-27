from rich.console import Console
from rich.markdown import Markdown
import json

# Initialize Rich Console
console = Console()

def preview_section(json_data, section):
    """
    Render a specific section of the resume based on user input.
    """
    if section == "summary":
        console.rule("[bold blue]Summary Section")
        summary_data = json_data.get("summary", {})
        static_content = summary_data.get("static_content", "")
        dynamic_content = summary_data.get("dynamic_content", "")
        summary_text = f"{static_content} {dynamic_content}".strip()
        if not summary_text:
            summary_text = "Summary not available."
        console.print(Markdown(f"**Summary:**\n{summary_text}"))

    elif section == "skills":
        console.rule("[bold blue]Skills Section")
        skills = json_data.get("skills", {})
        if "groups" in skills:
            for group in skills["groups"]:
                console.print(f"[bold]{group['group_name']}:[/bold] {', '.join(group['skills_list'])}")
        else:
            console.print("[italic]Skills not available.[/italic]")

    elif section == "experience":
        console.rule("[bold blue]Experience Section")
        experience = json_data.get("experience", {}).get("roles", [])
        if experience:
            for role in experience:
                console.print(f"[bold]{role['title']}[/bold] at [bold]{role['company']}[/bold]")
                console.print(f"[italic]{role['location']} | {role['dates']}[/italic]")
                for responsibility in role.get("responsibilities", []):
                    console.print(f"- {responsibility}")
        else:
            console.print("[italic]Experience not available.[/italic]")

    else:
        console.print("[red]Invalid section specified. Please choose from: summary, skills, experience.[/red]")

# Load JSON data
json_path = "test_data/resume.json"
with open(json_path, "r") as f:
    json_data = json.load(f)

# User chooses a section to preview
console.print("[bold green]Available sections: summary, skills, experience[/bold green]")
section_to_preview = input("Enter the section you'd like to preview: ").strip().lower()
preview_section(json_data, section_to_preview)
