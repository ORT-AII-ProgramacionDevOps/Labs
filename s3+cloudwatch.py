import boto3
import os
import time

# Configuración de AWS
s3 = boto3.client('s3')
cloudwatch_logs = boto3.client('logs')
ssm = boto3.client('ssm')
ec2 = boto3.client('ec2')

# Parámetros
bucket_name = '321r23uihr23uih2i3'
logs_directory = '/data_logs'
log_group = '/ec2/logs'
log_stream = 'upload_logs'

# Obtener el ID de las instancias que tienen el tag "Configured"
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Status', 'Values': ['Configured']}
    ]
)

instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

if not instance_ids:
    print('No se encontraron instancias con el tag "Configured".')
    exit(1)

instance_id = instance_ids[0]  # Usar la primera instancia encontrada
if not response['Tags']:
    print('La instancia no está etiquetada como "Configured".')
    exit(1)

def log_event(message):
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
    
    # Obtener el timestamp actual
    timestamp = int(time.time() * 1000)
    
    # Enviar el evento de log a CloudWatch
    cloudwatch_logs.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[
            {
                'timestamp': timestamp,
                'message': message
            }
        ]
    )

def upload_files_from_instance():
    # Ejecutar comando en la instancia EC2 para listar archivos en /data_logs
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [f'ls {logs_directory}']}
    )
    
    command_id = response['Command']['CommandId']
    
    # Esperar a que el comando se ejecute y obtener la salida
    time.sleep(5)
    output = ssm.get_command_invocation(
        CommandId=command_id,
        InstanceId=instance_id
    )
    
    if output['Status'] == 'Success':
        files_to_upload = output['StandardOutputContent'].split('\n')
        for file_name in files_to_upload:
            if file_name:
                file_path = os.path.join(logs_directory, file_name)
                
                # Descargar el archivo desde la instancia EC2
                ssm_response = ssm.send_command(
                    InstanceIds=[instance_id],
                    DocumentName='AWS-RunShellScript',
                    Parameters={'commands': [f'cat {file_path}']}
                )
                
                command_id = ssm_response['Command']['CommandId']
                time.sleep(5)
                file_output = ssm.get_command_invocation(
                    CommandId=command_id,
                    InstanceId=instance_id
                )
                
                if file_output['Status'] == 'Success':
                    file_content = file_output['StandardOutputContent']
                    
                    # Guardar el archivo localmente
                    local_file_path = f'/tmp/{file_name}'
                    with open(local_file_path, 'w') as f:
                        f.write(file_content)
                    
                    # Subir el archivo a S3
                    s3.upload_file(local_file_path, bucket_name, file_name)
                    print(f'Archivo {file_name} subido a {bucket_name}')
                    
                    # Registrar la subida en CloudWatch
                    log_event(f'Archivo {file_name} subido a S3 a las {time.ctime()}')
                else:
                    print(f'Error al obtener el contenido del archivo {file_name}')
    else:
        print('Error al listar archivos en el directorio /data_logs')

# Monitorear y subir archivos
while True:
    upload_files_from_instance()
    time.sleep(60)  # Esperar 1 minuto antes de volver a verificar