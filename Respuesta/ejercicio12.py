import boto3
import time

# Configuración de AWS
s3_client = boto3.client('s3')
logs_client = boto3.client('logs')
file_name = 'ejercicio1.py'


def main():
    # Parámetros
    bucket_name = 'mi-bucket-ejercicio12'
    log_group_name = 'nro-de-estudiante'
    log_stream_name = 'nro-de-estudiante'

    def crear_bucket(bucket_name):
        # Verificar si el bucket ya existe
        existing_buckets = s3_client.list_buckets()
        if not any(bucket['Name'] == bucket_name for bucket in existing_buckets['Buckets']):
            # Crear bucket S3
            s3_client.crear_bucket(Bucket=bucket_name)
        else:
            print(f'El bucket "{bucket_name}" ya existe.')

    # Crear log group
    # Verificar si el log group ya existe
    existing_log_groups = logs_client.describe_log_groups(logGroupNamePrefix=log_group_name)
    if not any(log_group['logGroupName'] == log_group_name for log_group in existing_log_groups['logGroups']):
        logs_client.create_log_group(logGroupName=log_group_name)
    else:
        print(f'El log group "{log_group_name}" ya existe.')

    # Verificar si el log stream ya existe
    existing_log_streams = logs_client.describe_log_streams(logGroupName=log_group_name, logStreamNamePrefix=log_stream_name)
    if not any(log_stream['logStreamName'] == log_stream_name for log_stream in existing_log_streams['logStreams']):
        logs_client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    else:
        print(f'El log stream "{log_stream_name}" ya existe.')

    # Función para subir archivo y loguear
    def subir_archivo(file_name, bucket, log_group, log_stream):
        # Subir archivo a S3
        s3_client.upload_file(file_name, bucket, file_name)

        # Generar entrada en el log stream
        log_message = f'Se subió el archivo "{file_name}"'
        logs_client.put_log_events(
            logGroupName=log_group,
            logStreamName=log_stream,
            logEvents=[
                {
                    'timestamp': int(time.time() * 1000),
                    'message': log_message
                }
            ]
        )

    # Crear bucket y subir archivo
    crear_bucket(bucket_name)
    subir_archivo(file_name, bucket_name, log_group_name, log_stream_name)

# Llamar a la función principal
main()