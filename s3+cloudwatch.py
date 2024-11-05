import boto3
import time
import os

bucket_name = '1497832jdew981'

# Crear cliente para S3 y EC2
s3 = boto3.client('s3')
ec2 = boto3.resource('ec2')
cloudwatch_logs = boto3.client('logs')
ssm = boto3.client('ssm')

def get_instance_id():
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instance = next(instances, None)
    if instance:
        print(f'ID de la instancia en ejecución: {instance.id}')
        return instance.id
    else:
        print('No hay instancias en ejecución.')
        return None

def create_bucket_if_not_exists(bucket_name):
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f'El bucket {bucket_name} ya existe.')
    except:
        s3.create_bucket(Bucket=bucket_name)
        print(f'Bucket {bucket_name} creado.')

def monitor_and_upload_logs(instance_id):
    instance = ec2.Instance(instance_id)
    
    # Verificar que la instancia tiene la etiqueta "Configured"
    configured_tag = next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Status'), None)
    
    if configured_tag == 'Configured':
        # Monitorear el directorio `/data_logs` (esto normalmente se haría en la instancia)
        logs_directory = ssm.send_command(
            InstanceIds=[instance_id],
            DocumentName='AWS-RunShellScript',
            Parameters={'commands': ['ls /data_logs']}
        )['Command']['Output']
        try:
            files_to_upload = os.listdir(logs_directory)
        except PermissionError as e:
            print(f'Error de permiso: {e}')
            return
        
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

# Crear el bucket si no existe
create_bucket_if_not_exists(bucket_name)

instance_id = get_instance_id()
if instance_id:
    monitor_and_upload_logs(instance_id)
else:
    print('No se puede monitorear ninguna instancia.')



