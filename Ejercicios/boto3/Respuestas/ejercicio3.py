import boto3

# Configura el cliente de S3
s3 = boto3.client('s3')

# Nombre del bucket
bucket_name = 'nombre-del-bucket'

# Lista los objetos en el bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Verifica si hay objetos en el bucket
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("No hay objetos en el bucket.")