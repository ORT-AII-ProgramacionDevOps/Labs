import boto3
import time
import os

# Crear cliente para S3 y EC2
s3 = boto3.client('s3')
ec2 = boto3.resource('ec2')
cloudwatch_logs = boto3.client('logs')

bucket_name = 'nombre-del-bucket-s3'

def monitor_and_upload_logs(instance_id):
    instance = ec2.Instance(instance_id)
    
    # Verificar que la instancia tiene la etiqueta "Configured"
    configured_tag = next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Status'), None)
    
    if configured_tag == 'Configured':
        # Monitorear el directorio `/data_logs` (esto normalmente se haría en la instancia)
        logs_directory = '/data_logs/'
        files_to_upload = os.listdir(logs_directory)
        
        for file_name in files_to_upload:
            file_path = os.path.join(logs_directory, file_name)
            
            # Subir el archivo a S3
            s3.upload_file(file_path, bucket_name, file_name)
            print(f'Archivo {file_name} subido a {bucket_name}')
            
            # Registrar la subida en CloudWatch
            log_event(f'Archivo {file_name} subido a S3 a las {time.ctime()}')
    else:
        print('La instancia no está configurada correctamente, no se pueden subir archivos')

def log_event(message):
    log_group = '/ec2/logs'
    log_stream = 'upload_logs'
    
    # Crear grupo de logs si no existe
    try:
        cloudwatch_logs.create_log_group(logGroupName=log_group)
    except cloudwatch_logs.exceptions.ResourceAlreadyExistsException:
        pass
    
    # Crear stream de logs si no existe
    try:
        cloudwatch_logs.create_log_stream(
            logGroupName=log_group,
            logStreamName=log_stream
        )
    except cloudwatch_logs.exceptions.ResourceAlreadyExistsException:
        pass
    
    # Publicar el evento en CloudWatch Logs
    cloudwatch_logs.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[{
            'timestamp': int(time.time() * 1000),
            'message': message
        }]
    )

# Asumiendo que la instancia ya está lanzada
monitor_and_upload_logs('i-xxxxxxxxxxxxxxxxx')  # Reemplaza por el ID de tu instancia