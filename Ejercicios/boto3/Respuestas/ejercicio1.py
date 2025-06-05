import boto3

s3_client = boto3.client('s3')

file_name = 'path/to/your/file'
bucket_name = 'your-bucket-name'
object_name = file_name.split('/')[-1]  # Extract the file name from the path  
try:    
    boto3.client('s3').create_bucket(Bucket=bucket_name)
except boto3.exceptions.S3CreateError as e:
    print(f"Error creating bucket: {e}")
    exit(1)
    
    s3_client.upload_file(file_name, bucket_name, object_name)

    print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
except FileNotFoundError:
    print(f"The file {file_name} was not found")