import boto3
import time

def ejercicio_11():
    ec2 = boto3.client('ec2')
    ssm = boto3.client('ssm')
    instance_params = {
        'ImageId': 'ami-063d43db0594b521b',
        'MinCount': 1,
        'MaxCount': 1,
        'UserData': open('userdata.sh').read(),
        'IamInstanceProfile': {
            'Name': 'LabInstanceProfile'
        },
         'TagSpecifications': [
             {
                 'ResourceType': 'instance',
                 'Tags': [
                     {
                     'Key': 'Name',
                     'Value': '270809'
                     },
                 ]
             },
         ]
    }
    
    try:
        response = ec2.run_instances(**instance_params)
    except Exception as e:
        print(e)
    
    instance_id = response['Instances'][0]['InstanceId']

    # Esperar a que la instancia esté en estado 'running'
    while True:
        instance_status = ec2.describe_instance_status(InstanceIds=[instance_id])
        if instance_status['InstanceStatuses']:
            system_status = instance_status['InstanceStatuses'][0]['SystemStatus']['Status']
            print(f'Estado del sistema: {system_status}')
            print()
            if system_status == 'ok':
                break
        time.sleep(10)

    command = 'ls -l /tmp/270809'
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]}
    )
    command_id = response['Command']['CommandId']
    
    time.sleep(5)
    
    output = ssm.get_command_invocation(
        CommandId=command_id,
        InstanceId=instance_id
    )

    print(output.get('Status'))

    command = 'id -u 2770809'
    
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]}
    )

    time.sleep(5)

    
    command = 'sudo '
    
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]}
    )

    time.sleep(5)

    output = ssm.get_command_invocation(
        CommandId = command_id,
        InstanceId = instance_id
    )

    print(output.get('Status'))

ejercicio_11()