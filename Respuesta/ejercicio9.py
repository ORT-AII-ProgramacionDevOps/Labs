import boto3

ec2 = boto3.client('ec2')

user_data_script = '''#!/bin/bash
sudo useradd Test
sudo mkdir /tmp/TestDirectory
'''

response = ec2.run_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
    MinCount=1,
    MaxCount=1,
    UserData=user_data_script
)
print("Instance created with ID:", response['Instances'][0]['InstanceId'])