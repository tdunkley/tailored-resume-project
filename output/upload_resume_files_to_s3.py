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

# Upload all files in the local directory to S3
for root, dirs, files in os.walk(local_dir):
    for file_name in files:
        local_path = os.path.join(root, file_name)
        s3_path = f"input/resumes/{file_name}"
        upload_file_to_s3(local_path, s3_path)
