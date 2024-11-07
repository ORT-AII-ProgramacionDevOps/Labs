# Ejercicios para empezar a trabajar con Boto3

## Ejercicio 1: Subir un archivo a S3
1. Crea un bucket de S3
2. Escriba un script que suba un archivo a tu bucket.

## Ejercicio 2: Descargar un archivo de S3
1. Escriba un script que descargue un archivo de tu bucket.

## Ejercicio 3: Listar objetos en un bucket
1. Escriba un script que liste todos los objetos en un bucket específico.

## Ejercicio 4: Eliminar un objeto de S3
1. Escriba un script que elimine un objeto de tu bucket.

## Ejercicio 5: Crear una instancia EC2
1. Escriba un script que cree una instancia EC2.

## Ejercicio 6: Obtener el ID de una instancia EC2
1. Escriba un script que obtenga y muestre el ID de una instancia EC2 específica.

## Ejercicio 7: Crear una instancia asignando el Instance Profile de LabRole
1. Escriba un script que cree una instancia EC2 y esta tenga asociado el Instance Profile del rol LabRole.

## Ejercicio 8: Enviar un comando a una instancia EC2 usando SSM
1. Escriba un script que envíe un comando a la instancia EC2 creada anteriormente.

## Ejercicio 9: Crear una instancia EC2 con un UserData que cree un usuario llamado Test y un directorio dentro de /tmp
1. Escriba un script que cree una instancia EC2 con un UserData que cree un usuario Test y una directorio dentro de /tmp.

## Ejercicio 10: Crear un Log Group y un Log Stream en CloudWatch
1. Escriba un script que cree un Log Group y un Log Stream en CloudWatch.
2. Envía un mensaje de prueba al Log Stream creado.

## Ejercicio 11: Crear una instancia EC2 con Tags, UserData y SSM para verificar 
1. Escriba un script con una funcion que cree una instancia EC2 con un Tag en la cual el valor Name debe ser igual a el nro de estudiante del alumno, un UserData que cree un usuario con el nombre del nombre del alumno y un directorio dentro de /tmp que se llame como el nro de estudiante este debe estar escrito en un script de bash en donde el script debe leer el contenido del mismo. Y por ultimo mediante SSM comprobar que las acciones se hayan efectuado con exito.

## Ejercicio 12: Generar un Bucket S3 subir un archivo y generar entrada en un logstream
1. Escriba un script que con una funcion que cree un bucket s3 a su vez que un logroup y logstream que de nombre tenga el nro de estudiante y cada vez que se suba un archivo a s3 se debe generar una entrada en el logstream con el siguiente mensaje: se subio el archivo "Nombre_de_archivo".