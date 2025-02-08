import boto3

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'resume-tailoring-storage'  # Replace with your actual S3 bucket name

def list_files_in_s3(prefix):
    """List files in S3 with a given prefix."""
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        if 'Contents' in response:
            files = [content['Key'] for content in response['Contents']]
            print(f"Files in {bucket_name}/{prefix}: {files}")
            return files
        else:
            print(f"No files found in {bucket_name}/{prefix}")
            return []
    except Exception as e:
        print(f"Error listing files in S3: {e}")
        return []

if __name__ == "__main__":
    prefix = 'input/resumes/'  # Replace with the actual prefix
    list_files_in_s3(prefix)
