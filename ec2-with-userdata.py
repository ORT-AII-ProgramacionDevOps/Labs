import boto3
import time

# Crear un cliente de EC2
ec2_client = boto3.client('ec2')
ssm_client = boto3.client('ssm')
ec2 = boto3.resource('ec2')  # Definir el cliente de recurso EC2
command = 'ls -l /aaa '

# Definir los parámetros para la instancia EC2
instance_params = {
    'ImageId': 'ami-06b21ccaeff8cd686',  
    #'InstanceType': 't2.micro',
    #'UserData': open('script.sh').read(),
    'MinCount': 1,
    'MaxCount': 1,  
    'IamInstanceProfile':{
        'Name': 'LabInstanceProfile'
    }
}

# Crear la instancia EC2
response = ec2_client.run_instances(**instance_params)
instance_id = response['Instances'][0]['InstanceId']

# Esperar a que la instancia esté en estado 'running'
while True:
    instance_status = ec2_client.describe_instance_status(InstanceIds=[instance_id])
    if instance_status['InstanceStatuses']:
        instance_state = instance_status['InstanceStatuses'][0]['InstanceState']['Name']
        system_status = instance_status['InstanceStatuses'][0]['SystemStatus']['Status']
        instance_status = instance_status['InstanceStatuses'][0]['InstanceStatus']['Status']
        print(f'Estado de la instancia: {instance_state}')
        print()
        print(f'Estado del sistema: {system_status}')
        print()
        print(f'Estado de la instancia: {instance_status}')
        print()
        if instance_state == 'running' and system_status == 'ok' and instance_status == 'ok':
            break
    time.sleep(10)

# Ejecutar comando en la instancia a través de SSM
response = ssm_client.send_command(
    InstanceIds=[instance_id],
    DocumentName='AWS-RunShellScript',
    Parameters={'commands': [command]}
)

command_id = response['Command']['CommandId']

# Esperar a que el comando termine
time.sleep(5)

# Obtener el resultado del comando
output = ssm_client.get_command_invocation(
    CommandId=command_id,
    InstanceId=instance_id
)

# Verificar el estado del comando
if output['Status'] == 'Success':
    status = 'Configured'  # Definir el valor de status
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[{'Key': 'Status', 'Value': status}]
    )
    print(f'Instancia etiquetada como {status}')
else:
    status = 'Misconfigured'  # Definir el valor de status
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[{'Key': 'Status', 'Value': status}]
    )
    print(f'Instancia etiquetada como {status}')