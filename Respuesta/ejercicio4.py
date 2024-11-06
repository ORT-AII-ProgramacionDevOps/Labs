import boto3

# Configura el cliente de S3
s3 = boto3.client('s3')

# Especifica el nombre del bucket y el objeto a eliminar
bucket_name = 'tu-nombre-de-bucket'
object_key = 'ruta/al/objeto'

# Elimina el objeto
s3.delete_object(Bucket=bucket_name, Key=object_key)

print(f'Objeto {object_key} eliminado del bucket {bucket_name}')