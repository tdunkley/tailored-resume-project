import boto3
import os

def upload_file_to_s3(file_path, bucket_name, s3_key):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded to {bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    file_path = "/c:/Users/troy_/Downloads/Tailored Resume Process/S3/resume_tdunkley.json"
    bucket_name = "your-bucket-name"
    s3_key = "path/to/resume_tdunkley.json"
    
    upload_file_to_s3(file_path, bucket_name, s3_key)
