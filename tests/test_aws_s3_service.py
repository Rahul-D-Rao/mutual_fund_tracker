import os
import sys
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Add the 'src/services' directory to sys.path to be able to import from it
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src', 'services')))

from aws_s3_service import upload_to_s3
import pytest
from unittest.mock import patch

@patch("boto3.client")
def test_upload_to_s3(mock_boto_client):
    mock_client_instance = mock_boto_client.return_value
    mock_client_instance.upload_file.return_value = None  # Simulate success

    try:
        upload_to_s3("datasets/output_results.csv", "test-bucket", "output_results.csv")
        mock_client_instance.upload_file.assert_called_once_with(
            "datasets/output_results.csv", "test-bucket", "output_results.csv"
        )
    except Exception as e:
        pytest.fail(f"Upload to S3 failed: {e}")
