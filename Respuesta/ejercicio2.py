import boto3

bucket_name = 'TU_BUCKET_NAME'
file_key = 'ruta/al/archivo/en/s3'
download_path = 'ruta/local/donde/descargar/el/archivo'

# Crear un cliente de S3
s3 = boto3.client('s3')

# Descargar el archivo
s3.download_file(bucket_name, file_key, download_path)

print(f'Archivo {file_key} descargado a {download_path}')