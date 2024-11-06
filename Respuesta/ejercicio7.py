import boto3

ec2 = boto3.resource('ec2')  # Definir el cliente de recurso EC2

# Definir los parámetros para la instancia EC2
instance_params = {
    'ImageId': 'ami-06b21ccaeff8cd686',  
    'InstanceType': 't2.micro',
    'MinCount': 1,
    'MaxCount': 1,  
    'IamInstanceProfile':{
        'Name': 'LabInstanceProfile'
    }
}

# Crear la instancia EC2
response = ec2.run_instances(**instance_params)