import boto3

def upload_to_s3(file_path, bucket_name, s3_key):
    """
    Upload a file to an AWS S3 bucket.

    Args:
        file_path (str): Path of the file to upload.
        bucket_name (str): Name of the S3 bucket.
        s3_key (str): S3 key for the uploaded file.

    Returns:
        None
    """
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id="AKIASVQKH62Y7WWHIKW2",
            aws_secret_access_key="Li3IQBdoY8E0JVnIhl4rfYqLbkGnatNlZPKZJtP1",
            region_name="us-east-2"  # Replace with your region
        )
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded to S3 bucket '{bucket_name}' with key '{s3_key}'.")
    except Exception as e:
        raise RuntimeError(f"Failed to upload file to S3: {e}")