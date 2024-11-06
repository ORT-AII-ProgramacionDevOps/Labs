import boto3

s3_client = boto3.client('s3')

file_name = 'path/to/your/file.txt'
bucket_name = 'your-bucket-name'
object_name = file_name  
try:    
    s3_client.upload_file(file_name, bucket_name, object_name)
    print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
except FileNotFoundError:
    print(f"The file {file_name} was not found")