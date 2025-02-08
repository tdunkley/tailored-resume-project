import boto3
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("s3_cleanup")

# Initialize S3 client
s3_client = boto3.client('s3')
bucket_name = "resume-tailoring-storage"

def list_files_in_s3(prefix):
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

def move_file_to_folder(s3_key, new_prefix):
    """Move a file to a new folder in the S3 bucket."""
    try:
        copy_source = {'Bucket': bucket_name, 'Key': s3_key}
        new_key = f"{new_prefix}/{s3_key.split('/')[-1]}"
        s3_client.copy_object(Bucket=bucket_name, CopySource=copy_source, Key=new_key)
        s3_client.delete_object(Bucket=bucket_name, Key=s3_key)
        logger.info(f"File {s3_key} moved to {new_key} in S3 bucket {bucket_name}.")
    except Exception as e:
        logger.error(f"Error moving file in S3: {e}", exc_info=True)
        raise

def cleanup_s3_bucket():
    """Cleanup the S3 bucket by deleting unnecessary files and organizing files into directories."""
    try:
        # List all files in the bucket
        files = list_files_in_s3("")

        # Example: Delete files older than 30 days and move important files to appropriate folders
        for file_key in files:
            # Add your logic to determine which files to delete or move
            if "old" in file_key:  # Example condition to delete files
                delete_file_from_s3(file_key)
            elif "data" in file_key:  # Example condition to move files to data folder
                move_file_to_folder(file_key, "data")
            elif "output" in file_key:  # Example condition to move files to output folder
                move_file_to_folder(file_key, "output")
            elif "scripts" in file_key:  # Example condition to move files to scripts folder
                move_file_to_folder(file_key, "scripts")
            elif "logs" in file_key:  # Example condition to move files to logs folder
                move_file_to_folder(file_key, "logs")
            elif "templates" in file_key:  # Example condition to move files to templates folder
                move_file_to_folder(file_key, "templates")

        logger.info("S3 bucket cleanup and organization completed successfully.")
    except Exception as e:
        logger.error(f"Error during S3 bucket cleanup: {e}", exc_info=True)

if __name__ == "__main__":
    cleanup_s3_bucket()
