import boto3
import logging
import os

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'resume-tailoring-storage'  # Replace with your actual S3 bucket name

def download_file_from_s3(bucket_name, s3_key, download_path):
    """Download a file from S3."""
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket_name, s3_key, download_path)
    logging.info(f"Downloaded {s3_key} from {bucket_name} to {download_path}")

if __name__ == "__main__":
    filename = 'input/resumes/full_cv.docx'  # Replace with the actual filename
    download_path = 'downloaded_full_cv.docx'
    download_file_from_s3(bucket_name, filename, download_path)
    print(f"Downloaded {filename} and saved as {download_path}")
