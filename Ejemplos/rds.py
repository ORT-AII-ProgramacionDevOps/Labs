import boto3

# Configuración de la base de datos RDS
rds_client = boto3.client('rds')

db_instance_identifier = 'mi-rds-ejemplo'
db_instance_class = 'db.t2.micro'
engine = 'mysql'
master_username = 'admin'
master_user_password = 'password1234'
allocated_storage = 20

try:
    response = rds_client.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_user_password,
        AllocatedStorage=allocated_storage
    )
    print(f"Creando instancia de base de datos RDS: {db_instance_identifier}")
    print(response)
except Exception as e:
    print(f"Error al crear la instancia de base de datos: {e}")