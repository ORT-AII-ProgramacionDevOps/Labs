import boto3
# Crea un cliente de EC2
ec2_client = boto3.client('ec2')

# Describe la instancia EC2 específica
response = ec2_client.describe_instances()

# Obtiene el ID de la instancia
print(response['Reservations'][0]['Instances'][0]['InstanceId'])