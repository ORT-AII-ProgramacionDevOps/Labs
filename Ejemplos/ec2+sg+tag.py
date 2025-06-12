import boto3
AMI = 'ami-06b21ccaeff8cd686' 
SECURITY_GROUP_NAME = 'pepito1'
DESCRIPTION = 'Security group para mi instancia EC2'
INSTANCE_NAME = 'Http-server' 

ec2 = boto3.client('ec2')

# Crear Security Group
response = ec2.create_security_group(
    GroupName=SECURITY_GROUP_NAME,
    Description=DESCRIPTION
)
sg_id = response['GroupId']

# Permitir SSH (puerto 22) desde cualquier lugar
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

# Crear la instancia EC2 y asociar el Security Group
instance = ec2.run_instances(
    ImageId=AMI,
    InstanceType='t2.micro',
    SecurityGroupIds=[sg_id],
    MinCount=1,
    MaxCount=1,
    UserData="""#!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "Hello, World!" > /var/www/html/index.html
    """,
    IamInstanceProfile={
        'Name': 'LabInstanceProfile'  # Cambia por tu perfil de instancia IAM si es necesario
    }
)
instance_id = instance["Instances"][0]["InstanceId"]

# Agregar tag Name a la instancia
ec2.create_tags(
    Resources=[instance_id],
    Tags=[{'Key': 'Name', 'Value': INSTANCE_NAME}]
)

print(f'Instancia creada con ID: {instance_id}')
print(f'Security Group creado con ID: {sg_id}')


ec2 = boto3.resource('ec2', region_name='us-east-1')  # Cambia la región si es necesario

instances = ec2.create_instances(
    ImageId=AMI,  # Cambia por el AMI ID que desees
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)
