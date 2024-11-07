import boto3
import time

# Configuración del cliente de S3 y CloudWatch
s3_client = boto3.client('s3')
logs_client = boto3.client('logs')

# Nombre del bucket, log group y log stream
nroestudiante = '12345'
bucket = f'student-{nroestudiante}-bucket'
log_group_name = f'student-{nroestudiante}-log-group'
log_stream_name = f'student-{nroestudiante}-log-stream'

def create_s3_bucket(bucket):
    s3_client.create_bucket(Bucket=bucket)
    print(f'Bucket {bucket} creado.')

def create_log_group_and_stream(log_group_name, log_stream_name):
    logs_client.create_log_group(logGroupName=log_group_name)
    logs_client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    print(f'Log group {log_group_name} y log stream {log_stream_name} creados.')

def upload_file_and_log(file_name, bucket, log_group_name, log_stream_name):
    s3_client.upload_file(file_name, bucket, file_name)
    print(f'Archivo {file_name} subido a {bucket}.')

    log_event = {
        'logGroupName': log_group_name,
        'logStreamName': log_stream_name,
        'logEvents': [
            {
                'timestamp': int(round(time.time() * 1000)),
                'message': f'Se subió el archivo "{file_name}".'
            }
        ]
    }
    logs_client.put_log_events(**log_event)
    print(f'Entrada de log creada para el archivo {file_name}.')

if __name__ == '__main__':
    create_s3_bucket(bucket)
    create_log_group_and_stream(log_group_name, log_stream_name)
    # Ejemplo de uso: subir un archivo y registrar en el log
    upload_file_and_log('example.txt', bucket, log_group_name, log_stream_name)