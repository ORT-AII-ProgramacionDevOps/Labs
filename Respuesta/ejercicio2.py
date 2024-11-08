import boto3

bucket_name = 'dwijdisojdaois'
file_key = 'snicolasg/home/sysadmin/DevOps/python/aws/file.txt'
download_path = '/home/gferradas/script-de-userdata'

# Crear un cliente de S3
s3 = boto3.client('s3')

# Descargar el archivo
s3.download_file(bucket_name, file_key, download_path)

print(f'Archivo {file_key} descargado a {download_path}')