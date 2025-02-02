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
    return json.loads(response['Body'].read())

# Example usage for testing
if __name__ == "__main__":
    # Example upload
    sample_data = {"section": "Personal Information", "rules": {"required_fields": ["Name", "Contact Info"]}}
    upload_to_s3(sample_data, 'resume.json')

    # Example download
    data = download_from_s3('resume.json')
    print(data)
