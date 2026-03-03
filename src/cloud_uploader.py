import boto3
from botocore.exceptions import NoCredentialsError
import os


AWS_ACCESS_KEY = "enter your access key here"
AWS_SECRET_KEY = "enter your secrect key here"
BUCKET_NAME = "sentinel-grid-anomalies"

def upload_anomaly_to_cloud(file_path, object_name=None):
    """
    Uploads a detected anomaly audio file to AWS S3.
    This fulfills the 'Global Reporting' part of our Architecture.
    """
    if object_name is None:
        object_name = os.path.basename(file_path)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    try:
        print(f"[CLOUD INFO] Infiltrating AWS S3... Uploading {file_path}")
        
        s3_client.upload_file(file_path, BUCKET_NAME, object_name)
        
        print(f"[SUCCESS] Anomaly report secured in Cloud: s3://{BUCKET_NAME}/{object_name}")
        return True

    except FileNotFoundError:
        print("[ERROR] The anomaly file was not found locally.")
        return False
    except NoCredentialsError:
        print("[ERROR] AWS Credentials not found. Check your IAM settings.")
        return False
    except Exception as e:
        print(f"[CRITICAL ERROR] Cloud infiltration failed: {e}")
        return False

if __name__ == "__main__":
    print("=== Project Sentinel-Grid: Cloud Integration Test ===")
    TEST_FILE = "../data/machine_sound.wav" 
    upload_anomaly_to_cloud(TEST_FILE)