import boto3
<<<<<<< HEAD
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("s3_manager")

# Initialize S3 client
s3_client = boto3.client('s3')

def upload_to_s3(file_path, s3_key, bucket_name="resume-tailoring-storage"):
    """Upload a file to an S3 bucket."""
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        logger.info(f"File {file_path} uploaded to S3 bucket {bucket_name} with key {s3_key}.")
    except Exception as e:
        logger.error(f"Error uploading file to S3: {e}", exc_info=True)
        raise

def download_from_s3(s3_key, bucket_name="resume-tailoring-storage"):
    """Download a file from an S3 bucket."""
    try:
        download_path = os.path.join("/tmp", os.path.basename(s3_key))
        s3_client.download_file(bucket_name, s3_key, download_path)
        logger.info(f"File {s3_key} downloaded from S3 bucket {bucket_name} to {download_path}.")
        return download_path
    except Exception as e:
        logger.error(f"Error downloading file from S3: {e}", exc_info=True)
        raise

def list_files_in_s3(prefix, bucket_name="resume-tailoring-storage"):
    """List files in an S3 bucket with a given prefix."""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        files = [content['Key'] for content in response.get('Contents', [])]
        logger.info(f"Files in S3 bucket {bucket_name} with prefix {prefix}: {files}")
        return files
    except Exception as e:
        logger.error(f"Error listing files in S3: {e}", exc_info=True)
        raise

def ensure_folder_structure(bucket_name="resume-tailoring-storage"):
    """Ensure the folder structure exists in the S3 bucket."""
    try:
        required_folders = ["input/resumes/", "output/resumes/"]
        for folder in required_folders:
            s3_client.put_object(Bucket=bucket_name, Key=(folder + '/'))
        logger.info(f"Folder structure ensured in S3 bucket {bucket_name}.")
    except Exception as e:
        logger.error(f"Error ensuring folder structure in S3: {e}", exc_info=True)
        raise

# Debug statement to confirm the file is being executed
print("s3_manager.py loaded successfully")
=======
import json

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'resume-tailoring-storage'  # Replace with your actual S3 bucket name

def upload_to_s3(data, filename):
    """Upload JSON data to S3."""
    s3.put_object(Bucket=bucket_name, Key=filename, Body=json.dumps(data, indent=4))
    print(f"Uploaded {filename} to S3.")

def download_from_s3(filename):
    """Download JSON data from S3."""
    response = s3.get_object(Bucket=bucket_name, Key=filename)
    return json.loads(response['Body'].read())

# Example usage for testing
if __name__ == "__main__":
    # Example upload
    sample_data = {"section": "Personal Information", "rules": {"required_fields": ["Name", "Contact Info"]}}
    upload_to_s3(sample_data, 'resume.json')

    # Example download
    data = download_from_s3('resume.json')
    print(data)
>>>>>>> 011eb20403b89d07c8ae11e5b4bc3094a262060f
