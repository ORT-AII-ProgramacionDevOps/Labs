import boto3
import time

s3=boto3.client('s3')
logs=boto3.client('logs')
file = "ec2.py"

def main():
    bucket_name="djwiofjewiofjskf"
    log_name="ewoifwoejfwe"
    
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        if bucket_name == bucket['Name']:
            print('Ya existe el bucket')
            exit(0)
    s3.create_bucket(Bucket=bucket_name)
    
    try:
        logs.create_log_group(logGroupName=log_name)
    except:   
        print('ya existe log group')
    
    response = logs.describe_log_streams(logGroupName=log_name, logStreamNamePrefix=log_name)
    try:
        logs.create_log_stream(logGroupName=log_name,logStreamName=log_name)
    except:   
        print('ya existe log string')
    
    

    s3.upload_file(file, bucket_name, file)
    mensaje_log = f'Se subio el archivo "{file}" '
    logs.put_log_events(
        logGroupName = log_name,
        logStreamName = log_name,
        logEvents = [
            {
                'timestamp': int(time.time() * 1000),
                'message': mensaje_log
            }
        ]
    )
    
main()
