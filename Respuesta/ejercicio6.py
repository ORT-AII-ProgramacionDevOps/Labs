import boto3

# Configura la región y el ID de la instancia
instance_id = 'i-0abcd1234efgh5678'

# Crea un cliente de EC2
ec2_client = boto3.client('ec2')

# Describe la instancia EC2 específica
response = ec2_client.describe_instances(InstanceIds=[instance_id])

# Obtiene el ID de la instancia
instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Muestra el ID de la instancia
print(f'El ID de la instancia es: {instance_id}')