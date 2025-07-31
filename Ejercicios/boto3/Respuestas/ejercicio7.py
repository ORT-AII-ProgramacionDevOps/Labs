import boto3

ec2 = boto3.client('ec2')

user_data = '''#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "¡Sitio personalizado!" > /var/www/html/index.html
'''

response = ec2.run_instances(
    ImageId='ami-06b21ccaeff8cd686',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    IamInstanceProfile={'Name': 'LabInstanceProfile'},
    UserData=user_data
)
instance_id = response['Instances'][0]['InstanceId']
print(f"Instancia creada con ID: {instance_id}")
