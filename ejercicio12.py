import boto3
import time

# Configuración de AWS
s3_client = boto3.client('s3')
logs_client = boto3.client('logs')
file_name = 'archivo.txt'


def setup_and_upload():
    # Parámetros
    bucket_name = 'mi-bucket-ejercicio12'
    log_group_name = 'nro-de-alumno-loggroup'
    log_stream_name = 'nro-de-alumno-logstream'

    def create_bucket(bucket_name):
        # Crear bucket S3
        s3_client.create_bucket(Bucket=bucket_name)

    # Crear log group
    logs_client.create_log_group(logGroupName=log_group_name)

    # Crear log stream
    logs_client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)

    # Función para subir archivo y loguear
    def upload_file_and_log(file_name, bucket, log_group, log_stream):
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
    create_bucket(bucket_name)
    upload_file_and_log(file_name, bucket_name, log_group_name, log_stream_name)

# Llamar a la función principal
setup_and_upload()