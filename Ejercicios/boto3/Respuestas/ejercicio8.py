import boto3
import botocore.exceptions as ClientError
ec2 = boto3.client('ec2')
# 1. Crear un Security Group que permita tráfico web desde cualquier IP
sg_name = 'web-sg-boto3'
try:
    response = ec2.create_security_group(
        GroupName=sg_name,
        Description='Permitir trafico web desde cualquier IP'
    )
    sg_id = response['GroupId']
    print(f"Security Group creado: {sg_id}")
    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )
except ClientError as e:
    if 'InvalidGroup.Duplicate' in str(e):
        sg_id = ec2.describe_security_groups(GroupNames=[sg_name])['SecurityGroups'][0]['GroupId']
        print(f"Security Group ya existe: {sg_id}")
    else:
        raise

# 2. Asociar el SG a la instancia EC2 creada anteriormente
# Obtener la primera instancia EC2 disponible
instances = ec2.describe_instances()
instance_id = instances['Reservations'][0]['Instances'][0]['InstanceId']

ec2.modify_instance_attribute(InstanceId=instance_id, Groups=[sg_id])
print(f"SG {sg_id} asociado a la instancia {instance_id}")

print("Ahora navegue a la IP pública de la instancia para verificar el acceso web.")
