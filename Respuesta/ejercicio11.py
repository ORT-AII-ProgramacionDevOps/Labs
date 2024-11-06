import boto3

# Configuración
student_number = "12345"
student_name = "nombre_del_alumno"
ami_id = "ami-0abcdef1234567890" 

# Leer el contenido del script desde un archivo
with open('script.sh', 'r') as file:
    user_data_script = file.read()

# Crear instancia EC2
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId=ami_id,
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': student_number
                }
            ]
        }
    ],
    UserData=user_data_script
)

instance_id = response['Instances'][0]['InstanceId']
print(f"Instancia creada con ID: {instance_id}")

# Comprobar con SSM
ssm = boto3.client('ssm')

# Comprobar usuario
command_user = f"getent passwd {student_name}"
response_user = ssm.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': [command_user]}
)
command_id_user = response_user['Command']['CommandId']

# Comprobar directorio
command_dir = f"ls /tmp/{student_number}"
response_dir = ssm.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': [command_dir]}
)
command_id_dir = response_dir['Command']['CommandId']

# Obtener resultados
output_user = ssm.get_command_invocation(
    CommandId=command_id_user,
    InstanceId=instance_id
)
output_dir = ssm.get_command_invocation(
    CommandId=command_id_dir,
    InstanceId=instance_id
)

print(f"Resultado de la comprobación del usuario: {output_user['StandardOutputContent']}")
print(f"Resultado de la comprobación del directorio: {output_dir['StandardOutputContent']}")