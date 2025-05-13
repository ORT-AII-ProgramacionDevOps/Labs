import boto3

bucket_name = 'test-bucket-prog-devops-2025'
file_key = 'script-de-userdata'
download_path = '/path/to/download/file'

# Crear un cliente de S3
s3 = boto3.client('s3')

# Descargar el archivo
s3.download_file(bucket_name, file_key, download_path)

print(f'Archivo {file_key} descargado a {download_path}')