import boto3
import os

# AWS S3 configuration
bucket_name = "resume-tailoring-storage"

def upload_to_s3(file_path, bucket_name, s3_key):
    try:
        s3 = boto3.client("s3")
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded to {bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")

if __name__ == "__main__":
    # File paths
    files_to_upload = {
        "job_description.txt": "c:/Users/troy_/Downloads/Tailored Resume Process/job_description.txt",
        "full_cv.docx": "c:/Users/troy_/Downloads/Tailored Resume Process/full_cv.docx",
        "master_resume.pdf": "c:/Users/troy_/Downloads/Tailored Resume Process/master_resume.pdf",
    }

    for s3_key, file_path in files_to_upload.items():
        if os.path.exists(file_path):
            upload_to_s3(file_path, bucket_name, s3_key)
        else:
            print(f"File not found: {file_path}")

