# Ejercicios para empezar a trabajar con Boto3

## Recursos adicionales
- [Guía de inicio rápido de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

## Ejercicio 1: Subir un archivo a S3
### Parte 1: Crear un bucket de S3
1. Escriba un script que cree un bucket de S3.

### Parte 2: Subir un archivo al bucket
1. Escriba un script que suba un archivo al bucket creado.

## Ejercicio 2: Descargar un archivo de S3
1. Escriba un script que descargue un archivo de un bucket específico.

## Ejercicio 3: Listar objetos en un bucket
1. Escriba un script que liste todos los objetos en un bucket específico.

## Ejercicio 4: Eliminar un objeto de S3
1. Escriba un script que elimine un objeto de un bucket específico.

## Ejercicio 5: Crear una instancia EC2
### Parte 1: Crear una instancia EC2 
1. Escriba un script que cree una instancia EC2.

### Parte 2: Obtener el ID de una instancia EC2
1. Escriba un script que obtenga y muestre el ID de una instancia EC2 específica.

### Parte 3: Crear una instancia con un Instance Profile
1. Escriba un script que cree una instancia EC2 asociada al Instance Profile del rol LabRole.

## Ejercicio 6: Enviar un comando a una instancia EC2 usando SSM
### Parte 1: Crear una instancia EC2
1. Cree una instancia EC2.

### Parte 2: Enviar un comando y extraer el resultado
1. Envíe un comando `echo "Hello world"` a la instancia EC2 creada anteriormente y extraiga el resultado.

## Ejercicio 7: Crear una instancia EC2 con UserData
1. Escriba un script que cree una instancia EC2 con un UserData que:
    - Cree un usuario llamado `Test`.
    - Cree el directorio dentro de `/tmp/nro-de-estudiante`.

## Ejercicio 8: Trabajar con CloudWatch Logs
### Parte 1: Crear un Log Group y un Log Stream
1. Escriba un script que cree un Log Group y un Log Stream en CloudWatch.

### Parte 2: Enviar un mensaje de prueba
1. Envíe un mensaje de prueba al Log Stream creado.

## Ejercicio 9: Crear una base de datos RDS y conectarse desde una instancia EC2
### Parte 1: Configurar el Security Group
1. Cree un Security Group que permita el acceso al puerto 3306 (MySQL) desde una instancia EC2.

### Parte 2: Crear una base de datos RDS
1. Escriba un script que cree una base de datos RDS MySQL utilizando el Security Group creado.

### Parte 3: Configurar la instancia EC2
1. Lanza una instancia EC2 en la misma VPC que la base de datos RDS.
2. Instale un cliente MySQL en la instancia EC2.

### Parte 4: Conectarse a la base de datos
1. Conéctese a la base de datos RDS desde la instancia EC2 utilizando el cliente MySQL.