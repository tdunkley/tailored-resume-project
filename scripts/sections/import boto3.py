import boto3
import json

# Set up S3 client using boto3
s3 = boto3.client('s3')

def load_resume_data_from_s3(bucket_name, object_key):
    """
    Downloads the resume.json file from S3 and loads it as a dictionary.
    
    Args:
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key (path) to the resume.json file in the bucket.
    
    Returns:
        dict: Loaded resume data.
    """
    try:
        # Download the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        
        # Read the file content and load as JSON
        resume_data = json.loads(response['Body'].read().decode('utf-8'))
        
        # Return the loaded data
        return resume_data
    
    except Exception as e:
        print(f"Error loading resume data from S3: {e}")
        raise

# Replace these values with your actual S3 bucket details
bucket_name = "resume-tailoring-storage"  # S3 bucket name
object_key = "resume.json"   # The path to resume.json within the S3 bucket

# Fetch resume data from S3 dynamically
resume_data = load_resume_data_from_s3(bucket_name, object_key)

# Print the loaded data to verify it's working
print(json.dumps(resume_data, indent=4))  # This prints the loaded data for debugging
