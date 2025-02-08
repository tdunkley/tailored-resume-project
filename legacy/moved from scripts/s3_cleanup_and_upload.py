import boto3
import logging
import os
import subprocess

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("s3_cleanup_and_upload")

# Initialize S3 client
s3_client = boto3.client('s3')
bucket_name = "resume-tailoring-storage"

def list_files_in_s3(prefix=""):
    """List files in an S3 bucket with a given prefix."""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        files = [content['Key'] for content in response.get('Contents', [])]
        logger.info(f"Files in S3 bucket {bucket_name} with prefix {prefix}: {files}")
        return files
    except Exception as e:
        logger.error(f"Error listing files in S3: {e}", exc_info=True)
        raise

def delete_file_from_s3(s3_key):
    """Delete a file from an S3 bucket."""
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=s3_key)
        logger.info(f"File {s3_key} deleted from S3 bucket {bucket_name}.")
    except Exception as e:
        logger.error(f"Error deleting file from S3: {e}", exc_info=True)
        raise

def delete_all_files_in_s3():
    """Delete all files in the S3 bucket."""
    try:
        files = list_files_in_s3()
        for file_key in files:
            delete_file_from_s3(file_key)
        logger.info("All files deleted from S3 bucket.")
    except Exception as e:
        logger.error(f"Error deleting all files from S3: {e}", exc_info=True)

def upload_local_files_to_s3(local_dir, s3_prefix):
    """Upload local files to the S3 bucket, maintaining the directory structure."""
    try:
        # Correct the path format for subprocess.run
        local_dir = os.path.normpath(local_dir)
        subprocess.run(["aws", "s3", "cp", local_dir, f"s3://{bucket_name}/{s3_prefix}", "--recursive"], check=True)
        logger.info(f"Local files from {local_dir} uploaded to S3 bucket {bucket_name} with prefix {s3_prefix}.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error uploading local files to S3: {e}", exc_info=True)
        raise

def cleanup_and_upload():
    """Cleanup the S3 bucket and upload local files."""
    try:
        # Delete all files in the S3 bucket
        delete_all_files_in_s3()

        # Upload local files to S3
        local_base_dir = "c:/Users/troy_/Downloads/Tailored Resume Process/S3"
        upload_local_files_to_s3(os.path.join(local_base_dir, "data"), "data")
        upload_local_files_to_s3(os.path.join(local_base_dir, "output"), "output")
        upload_local_files_to_s3(os.path.join(local_base_dir, "scripts"), "scripts")
        upload_local_files_to_s3(os.path.join(local_base_dir, "logs"), "logs")
        upload_local_files_to_s3(os.path.join(local_base_dir, "templates"), "templates")

        logger.info("S3 bucket cleanup and upload completed successfully.")
    except Exception as e:
        logger.error(f"Error during S3 bucket cleanup and upload: {e}", exc_info=True)

if __name__ == "__main__":
    cleanup_and_upload()
