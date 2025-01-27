# Tailored Resume Project

## Purpose
The **Tailored Resume Project** is designed to automate the process of resume generation, validation, and formatting by leveraging predefined JSON business rules. The project ensures that resume sections adhere to specific content and formatting requirements while maintaining consistency and scalability.

## Features
- **Sectional Testing Workflow**: Validate individual resume sections for content and formatting rules.
- **JSON Architecture**: Centralized business rules for managing content and formatting dynamically.
- **Inline Previews**: Review each resume section visually before generating Word documents.
- **Version Control**: Automated Git integration to track validated changes and scripts.

## Repository Structure
```
resume_project/
├── scripts/            # Python scripts for sectional testing and automation
├── data/               # JSON files containing resume data and business rules
├── outputs/            # Generated outputs (HTML previews, Word files)
├── tests/              # Unit and integration tests
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── setup.sh            # Automated environment setup script
```

## Workflow
1. **Inline Preview**: Render and review each resume section visually in the chat or browser.
2. **Word Generation**: Generate Word files after approving the section preview.
3. **Git Integration**: Automatically save, commit, and push validated changes to GitHub.

## Getting Started

### Prerequisites
- Install Python 3.10+.
- Ensure Git is installed and configured.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/tdunkley/tailored-resume-project.git
   cd tailored-resume-project
   ```

2. Set up the virtual environment and install dependencies:
   ```bash
   bash setup.sh
   ```

3. Run a sectional test:
   ```bash
   python scripts/test_personal_info.py
   ```

## How It Works
### Sectional Testing Workflow
- **Inline Preview**: Each section is rendered for review.
- **Approval Process**: Sections are approved or rejected for adjustments.
- **Word File Generation**: Approved sections are converted into Word format for validation.
- **Git Automation**: Finalized scripts and outputs are committed and pushed to the repository.

### JSON Business Rules
- **Content Rules**: Define placeholders, dynamic content, and static text.
- **Formatting Rules**: Specify font size, alignment, line spacing, and capitalization.

### Key Features
- **Consistent**: Outputs follow defined JSON rules.
- **Reliable**: Validates data and formatting for each section.
- **Automated**: Reduces manual intervention via scripts and Git integration.
- **Scalable**: JSON schema supports adding new sections dynamically.

## Contributions
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a detailed description of the changes.

## License
This project is licensed under the [MIT License](LICENSE).

