import boto3

# Configura el cliente de SSM y EC2
ec2_client = boto3.client('ec2', region_name='us-east-1')
ssm_client = boto3.client('ssm', region_name='us-east-1')

response = ec2_client.describe_instances()
instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Espera a que la instancia esté en estado 'running'
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

command = "echo 'Hola, mundo!'"

response = ssm_client.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': [command]}
)

command_id = response['Command']['CommandId']

# Espera a que el comando termine usando waiter personalizado
while True:
    output = ssm_client.get_command_invocation(
        CommandId=command_id,
        InstanceId=instance_id
    )
    if output['Status'] in ['Success', 'Failed', 'Cancelled', 'TimedOut']:
        break

print("Output:")
print(output['StandardOutputContent'])
