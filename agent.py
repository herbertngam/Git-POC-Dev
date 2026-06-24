import boto3

def list_s3_objects(bucket_name):
    """List all objects in an S3 bucket using boto3."""
    s3_client = boto3.client('s3')
    
    try:
        paginator = s3_client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name)
        
        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    print(f"Key: {obj['Key']}, Size: {obj['Size']}, LastModified: {obj['LastModified']}")
    except Exception as e:
        print(f"Error listing objects: {e}")

if __name__ == "__main__":
    bucket_name = "your-bucket-name"
    list_s3_objects(bucket_name)
    



