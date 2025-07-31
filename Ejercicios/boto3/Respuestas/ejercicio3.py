import boto3

# Nombre de bucket por defecto (puedes cambiarlo aquí si lo deseas)
BUCKET_NAME = 'mi-bucket-ejemplo-boto3'

def listar_objetos(bucket_name=BUCKET_NAME):
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print("No hay objetos en el bucket.")
    except Exception as e:
        print(f"Error listando objetos en el bucket '{bucket_name}': {e}")

if __name__ == "__main__":
    listar_objetos()