import boto3
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
    content = response['Body'].read()
    try:
        return json.loads(content.decode('utf-8'))
    except json.JSONDecodeError:
        return content  # Return binary content if not JSON

def list_files_in_s3(prefix):
    """List files in S3 with a given prefix."""
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        files = [content['Key'] for content in response.get('Contents', [])]
        print(f"Files in {bucket_name}/{prefix}: {files}")
        return files
    except Exception as e:
        print(f"Error listing files in S3: {e}")
        return []

def create_folder_in_s3(folder_name):
    """Create a folder in S3."""
    if not folder_name.endswith('/'):
        folder_name += '/'
    s3.put_object(Bucket=bucket_name, Key=folder_name)
    print(f"Created folder {folder_name} in S3.")

def ensure_folder_structure():
    """Ensure the required folder structure exists in S3."""
    folders = [
        'input/resumes/',
        'input/huntr/',
        'output/resumes/',
        'output/logs/'
    ]
    for folder in folders:
        create_folder_in_s3(folder)

# Example usage for testing
if __name__ == "__main__":
    # Ensure folder structure
    ensure_folder_structure()

    # Example upload
    sample_data = {"section": "Personal Information", "rules": {"required_fields": ["Name", "Contact Info"]}}
    upload_to_s3(sample_data, 'output/resumes/resume.json')

    # Example download
    data = download_from_s3('output/resumes/resume.json')
    print(data)

    # Example list files
    files = list_files_in_s3('input/resumes/')
    print(files)
