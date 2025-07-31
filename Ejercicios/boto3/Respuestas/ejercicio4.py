import boto3

# Configura el cliente de S3
s3 = boto3.client('s3')

# Parámetros por defecto
bucket_name = 'mi-bucket-ejemplo-boto3'
object_key = 'archivo.txt'

# Intenta eliminar el objeto
try:
    s3.delete_object(Bucket=bucket_name, Key=object_key)
    print(f'Objeto {object_key} eliminado del bucket {bucket_name}')
except Exception as e:
    print(f'Error eliminando objeto: {e}')