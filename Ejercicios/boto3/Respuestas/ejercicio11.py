import boto3
import botocore.exceptions

secretsmanager = boto3.client('secretsmanager')

SECRET_NAME = 'app/dev/api-key'
SECRET_VALUE = 'api-key-demo-123456'

try:
    secretsmanager.create_secret(
        Name=SECRET_NAME,
        SecretString=SECRET_VALUE
    )
    print(f"Secreto creado: {SECRET_NAME}")
except secretsmanager.exceptions.ResourceExistsException:
    secretsmanager.put_secret_value(
        SecretId=SECRET_NAME,
        SecretString=SECRET_VALUE
    )
    print(f"El secreto ya existia. Se actualizo el valor de: {SECRET_NAME}")

response = secretsmanager.get_secret_value(SecretId=SECRET_NAME)

print(f"Valor del secreto: {response['SecretString']}")
