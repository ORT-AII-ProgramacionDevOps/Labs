import boto3

# Reemplaza con tus valores
GROUP_NAME = 'MySecurityGroup'
DESCRIPTION = 'Security group for my application'
VPC_ID = 'vpc-xxxxxxxx'

ec2 = boto3.client('ec2')

try:
    # Crear el grupo de seguridad
    response = ec2.create_security_group(
        GroupName=GROUP_NAME,
        Description=DESCRIPTION,
        VpcId=VPC_ID
    )
    security_group_id = response['GroupId']
    print(f'Security Group Created: {security_group_id}')

    # Agregar una regla SSH (puerto 22)
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Permitir desde cualquier IP
            }
        ]
    )
    print('SSH rule added to the security group.')

except Exception as e:
    print(f'Error creating security group: {e}')

    try:
        # Crear un nuevo grupo de seguridad
        new_group_response = ec2.create_security_group(
            GroupName='MyNewSecurityGroup',
            Description='Security group allowing traffic from MySecurityGroup',
            VpcId=VPC_ID
        )
        new_security_group_id = new_group_response['GroupId']
        print(f'New Security Group Created: {new_security_group_id}')

        # Agregar una regla para permitir tráfico desde el grupo de seguridad anterior
        ec2.authorize_security_group_ingress(
            GroupId=new_security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': '-1',  # Todos los protocolos
                    'UserIdGroupPairs': [
                        {
                            'GroupId': security_group_id
                        }
                    ]
                }
            ]
        )
        print('Rule added to allow traffic from the previous security group.')

    except Exception as e:
        print(f'Error creating or modifying the new security group: {e}')
