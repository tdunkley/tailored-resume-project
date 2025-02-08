import json
import logging
import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Ensure s3_manager is imported correctly
try:
    from s3_manager import upload_to_s3, download_from_s3, list_files_in_s3, ensure_folder_structure
except ImportError as e:
    logger.error(f"Error importing s3_manager: {e}", exc_info=True)
    sys.exit(1)

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("bootstrap")

REQUIRED_FILES = [
    "config.json",
    "resume.json",
    "scripts/tracker.py",
    "scripts/section_processor.py",
    "scripts/validation_engine.py",
    "scripts/config_core.py"
]

REQUIRED_FUNCTIONS = {
    "tracker": ["log_event"],
    "section_processor": ["process_sections"],
    "validation_engine": ["validate_global_rules", "validate_cross_sectional_rules"],
    "config_core": ["get_paths", "setup_logging", "load_json", "validate_json_schema"]
}

def validate_dependencies():
    """Validate that all required files and functions exist."""
    logger.info("Validating dependencies...")
    missing_files = [file for file in REQUIRED_FILES if not os.path.exists(os.path.join(current_dir, file))]
    if missing_files:
        logger.error(f"Missing files: {', '.join(missing_files)}")
        sys.exit(1)
    missing_functions = []
    for module_name, functions in REQUIRED_FUNCTIONS.items():
        try:
            module = __import__(module_name)
            for func in functions:
                if not hasattr(module, func):
                    missing_functions.append(f"{func} in {module_name}")
        except ImportError as e:
            missing_functions.append(f"Module {module_name} could not be imported: {str(e)}")
    if missing_functions:
        logger.error(f"Missing functions or modules: {', '.join(missing_functions)}")
        sys.exit(1)
    logger.info("All dependencies validated successfully.")

def process_file(file_key, bucket_name, output_dir, config):
    try:
        download_path = os.path.join(output_dir, os.path.basename(file_key))
        resume_data = download_from_s3(file_key)
        if isinstance(resume_data, bytes):
            with open(download_path, 'wb') as f:
                f.write(resume_data)
        else:
            with open(download_path, 'w') as f:
                json.dump(resume_data, f, indent=4)
            validate_json_schema(resume_data, config["resume_schema"])
            validate_global_rules(resume_data, config)
            validate_cross_sectional_rules(resume_data, config)
            for section_name in resume_data.get("sections", {}).keys():
                process_sections(section_name, resume_data, output_dir)
            upload_to_s3(resume_data, f"output/resumes/{os.path.basename(file_key)}")
    except Exception as e:
        log_event("File Processing Error", "ERROR", f"An error occurred: {e}", logging.ERROR)
        logger.error(f"An error occurred during file processing: {e}", exc_info=True)

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def validate_config(config):
    required_keys = ["validation", "paths", "resume_schema", "formatting", "logging", "ci_cd"]
    for key in required_keys:
        if key not in config:
            logger.error(f"Missing required config key: {key}")
            return False
    return True

def setup_directories(paths):
    for key, path in paths.items():
        Path(path).mkdir(parents=True, exist_ok=True)
        logger.info(f"Directory {path} is set up.")

def main():
    """Main bootstrap process."""
    try:
        log_event("Bootstrap Initialization", "START", "Initializing bootstrap process...")
        validate_dependencies()
        paths = get_paths()
        config = load_config(os.path.join(current_dir, "config.json"))

        if not validate_config(config):
            logger.error("Configuration validation failed.")
            sys.exit(1)

        setup_directories(config["paths"])

        # Ensure folder structure in S3
        ensure_folder_structure()

        # Extract data from existing resume and populate resume.json
        doc_path = "c:/Users/troy_/Downloads/Tailored Resume Process/S3/full_cv.docx"  # Replace with the actual path to your Word document
        try:
            logger.info(f"Extracting data from resume: {doc_path}")
            resume_data = extract_resume_data(doc_path)
            save_resume_data(resume_data, paths["resume_json"])
            logger.info(f"Resume data extracted and saved to {paths['resume_json']}")
        except Exception as e:
            logger.error(f"Error extracting resume data: {e}", exc_info=True)

        resume_data = load_json(paths["resume_json"])

        # Example schema validation (define your schema as needed)
        resume_schema = {
            "type": "object",
            "properties": {
                "sections": {"type": "object"},
                # Add more schema definitions as needed
            },
            "required": ["sections"]
        }
        validate_json_schema(resume_data, resume_schema)

        # Process Huntr CSV file
        huntr_csv_file = os.path.join(current_dir, "huntr_job_applications.csv")  # Ensure the path is correct
        try:
            logger.info(f"Processing Huntr CSV file: {huntr_csv_file}")
            job_descriptions = process_huntr_csv(huntr_csv_file)
            save_job_descriptions(job_descriptions, "huntr_job_descriptions.json")
            logger.info("Huntr job descriptions saved to huntr_job_descriptions.json")
        except Exception as e:
            logger.error(f"Error processing Huntr CSV file: {e}", exc_info=True)

        # List files in S3 input folder
        bucket_name = "resume-tailoring-storage"
        input_prefix = "input/resumes/"
        try:
            logger.info(f"Listing files in S3 bucket: {bucket_name} with prefix: {input_prefix}")
            files = list_files_in_s3(input_prefix)
        except Exception as e:
            logger.error(f"Error listing files in S3 bucket: {e}", exc_info=True)

        # Process files in parallel
        try:
            with ThreadPoolExecutor(max_workers=5) as executor:
                for file_key in files:
                    executor.submit(process_file, file_key, bucket_name, paths["output_dir"], config)
            logger.info("Files processed successfully in parallel.")
        except Exception as e:
            logger.error(f"Error processing files in parallel: {e}", exc_info=True)

        log_event("Bootstrap Initialization", "END", "Bootstrap process completed successfully.")
    except Exception as e:
        log_event("Bootstrap Error", "ERROR", f"An error occurred: {e}", logging.ERROR)
        logger.error(f"An error occurred during the bootstrap process: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
