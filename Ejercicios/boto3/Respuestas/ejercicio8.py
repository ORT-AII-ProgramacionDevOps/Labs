import boto3
import time

# Configura el cliente de SSM
ec2_client = boto3.client('ec2', region_name='us-east-1')
ssm_client = boto3.client('ssm', region_name='us-east-1')

response = ec2_client.describe_instances()

# ID de la instancia EC2
instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Comando que se enviará a la instancia
command = "echo 'Hola, mundo!'"

# Enviar el comando a la instancia EC2
response = ssm_client.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': [command]}
)

# Obtener el Command ID
command_id = response['Command']['CommandId']

# Esperar a que el comando se ejecute
time.sleep(5)

# Obtener el resultado del comando
output = ssm_client.get_command_invocation(
    CommandId=command_id,
    InstanceId=instance_id
)

# Imprimir el output del comando
print("Output:")
print(output['StandardOutputContent'])