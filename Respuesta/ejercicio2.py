import boto3

bucket_name = 'dwijdisojdaois'
file_key = 'script-de-userdata'
download_path = '/home/gferradas/script-de-userdata'

# Crear un cliente de S3
s3 = boto3.client('s3')

# Creacion de bucket

s3.create_bucket(Bucket=bucket_name)

# Descargar el archivo
s3.download_file(bucket_name, file_key, download_path)

print(f'Archivo {file_key} descargado a {download_path}')