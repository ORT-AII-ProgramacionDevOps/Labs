import boto3

ec2 = boto3.client('ec2')  # Usar cliente en lugar del recurso

# Definir los parámetros para la instancia EC2
instance_params = {
    'ImageId': 'ami-06b21ccaeff8cd686',  
    'InstanceType': 't2.micro',
    'MinCount': 1,
    'MaxCount': 1,  
    'IamInstanceProfile': {
        'Name': 'LabInstanceProfile'
    },
    'UserData': """#!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "Hello, World!" > /var/www/html/index.html
    """
}

# Crear la instancia EC2
response = ec2.run_instances(**instance_params)
