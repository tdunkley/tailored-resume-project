import os
import sys
import logging
from pathlib import Path

# Dynamically add the core module path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(current_dir, "..")))

from core import get_paths, load_resume_data, setup_logging
from validation_engine import validate_sectional_rules

# Configure logging
logger = logging.getLogger(__name__)
setup_logging()

try:
    # Step 1: Retrieve paths
    logger.info("Retrieving paths...")
    paths = get_paths()

    # Step 2: Load resume data
    logger.info("Loading resume data...")
    resume_data = load_resume_data(paths["resume_json"])
    logger.info("Resume data loaded successfully.")

    # Step 3: Extract summary section
    logger.info("Extracting summary data...")
    summary_data = resume_data["sections"].get("summary")
    if not summary_data:
        raise ValueError("Summary section is missing in the JSON.")

    # Step 4: Validate summary data
    logger.info("Validating summary data...")
    validation_errors = validate_sectional_rules("summary", summary_data)
    if validation_errors:
        logger.error(f"Validation errors in summary: {validation_errors}")
        raise ValueError("Validation failed for summary section.")

    # Step 5: Format summary content
    logger.info("Formatting summary content...")
    formatting = summary_data.get("formatting", {})
    line_spacing_before = formatting.get("line_spacing", {}).get("before", 1)
    line_spacing_after = formatting.get("line_spacing", {}).get("after", 1)
    font_style = formatting.get("font_style", "regular").lower()

    # Combine static and dynamic content into a single paragraph
    static_content = summary_data.get("static_content", "").strip()
    dynamic_content = summary_data.get("dynamic_content", "").strip()
    full_summary = f"{static_content} {dynamic_content}".strip()

    # Prepare content
    section_header = "SUMMARY"
    formatted_summary = f"{section_header}\n\n{full_summary}"

    # Apply line spacing before and after
    final_output = (
        "\n" * line_spacing_before +
        formatted_summary +
        "\n" * line_spacing_after
    ).strip()

    # Step 6: Write output to file
    output_dir = Path(paths["output_dir"])
    output_file = output_dir / "summary.txt"
    output_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    with open(output_file, "w") as file:
        file.write(final_output)

    logger.info(f"Summary section output written successfully to: {output_file}")

except Exception as e:
    logger.error(f"An error occurred in summary.py: {e}", exc_info=True)
