import boto3
import logging

# Initialize the S3 client
s3 = boto3.client('s3')

def load_resume_data_from_s3(bucket_name, s3_key):
    """Load resume data from S3."""
    response = s3.get_object(Bucket=bucket_name, Key=s3_key)
    data = response['Body'].read().decode('utf-8')
    logging.info(f"Loaded resume data from S3 bucket {bucket_name} with key {s3_key}")
    return data

# ...existing code...
