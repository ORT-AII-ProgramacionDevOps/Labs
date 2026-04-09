import boto3

ssm = boto3.client('ssm')

PARAMETER_NAME = '/app/dev/database_url'
PARAMETER_VALUE = 'mysql://admin:password123@db.example.com:3306/app'

ssm.put_parameter(
    Name=PARAMETER_NAME,
    Value=PARAMETER_VALUE,
    Type='String',
    Overwrite=True
)

response = ssm.get_parameter(Name=PARAMETER_NAME)

print(f"Parametro creado o actualizado: {PARAMETER_NAME}")
print(f"Valor del parametro: {response['Parameter']['Value']}")
