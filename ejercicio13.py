import boto3
import time

s3=boto3.client('s3')
logs=boto3.client('logs')

bucket_name="prog-devops2024-ejericio13"

log_name="Progdevops2024"

buckets = s3.list_buckets()

def bucket():
    for bucket in buckets['Buckets']:
        if bucket_name == bucket['Name']:
            print('Ya existe el bucket')
            return
    s3.create_bucket(Bucket=bucket_name)

bucket()

try:
    logs.create_log_group(logGroupName=log_name)
except:   
    print('ya existe log group')

file=input('Ingrese nombre de archivo a subir')

response = logs.describe_log_streams(logGroupName=log_name, logStreamNamePrefix=log_name)

if not any(response['logStreams']):
    logs.create_log_stream(logGroupName=log_name,logStreamName=log_name)
else:
    print('Ya existe log stream')

s3.upload_file(file, bucket_name, file)

logs.put_log_events(
    logGroupName = log_name,
    logStreamName = log_name,
    logEvents = [
        {
            'timestamp': int(time.time() * 1000),
            'message': f'Se subio {file} '
        }
    ]
)