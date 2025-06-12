import boto3
import os

# Configuración de la base de datos RDS
rds_client = boto3.client('rds')

db_instance_identifier = 'mi-rds-ejemplo'
db_instance_class = 'db.t3.medium'  # Cambiado a una clase soportada
engine = 'mariadb'
engine_version = '10.6.14'  # Especifica una versión soportada de MariaDB
master_username = 'admin'
master_user_password = open("password.txt", 'r').read().strip()  # Asegúrate de que el archivo password.txt contenga la contraseña
allocated_storage = int(os.environ.get('RDS_ALLOCATED_STORAGE', 20))
publicly_accessible = True

try:
    response = rds_client.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        EngineVersion=engine_version,
        MasterUsername=master_username,
        MasterUserPassword=master_user_password,
        AllocatedStorage=allocated_storage
    )
    print(f"Creando instancia de base de datos RDS: {db_instance_identifier}")
except Exception as e:
    print(f"Error al crear la instancia de base de datos: {e}")