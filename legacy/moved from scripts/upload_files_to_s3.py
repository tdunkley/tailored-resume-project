import os
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'resume-tailoring-storage'  # Replace with your actual S3 bucket name

def upload_file_to_s3(local_path, s3_path):
    """Upload a file to S3."""
    with open(local_path, 'rb') as file:
        s3.upload_fileobj(file, bucket_name, s3_path)
    print(f"Uploaded {local_path} to {s3_path} in S3.")

# Define the local directory and S3 bucket details
local_dir = "c:/Users/troy_/Downloads/Tailored Resume Process/S3"

# List of files to upload
files_to_upload = [
    "resume.json",
    "config.json",
    "huntr_job_applications.csv",
    "scripts/s3_manager.py",
    "scripts/config_core.py",
    "scripts/tracker.py",
    "scripts/section_processor.py",
    "scripts/validation_engine.py",
    "scripts/job_description_fetcher.py",
    "scripts/resume_parser.py",
    "scripts/full_resume_generator.py"
]

# Upload files to S3
for file_name in files_to_upload:
    local_path = os.path.join(local_dir, file_name)
    s3_path = file_name.replace("\\", "/")  # Ensure correct S3 path format
    upload_file_to_s3(local_path, s3_path)
