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

## Ejercicio 6: Enviar un comando a una instancia EC2 usando SSM
### Parte 1: Crear una instancia EC2
1. Escriba un script que cree una instancia EC2 asociada al Instance Profile del rol LabRole.

### Parte 2: Enviar un comando y extraer el resultado
1. Envíe un comando `echo "Hello world"` a la instancia EC2 creada anteriormente y extraiga el resultado.

## Ejercicio 7: Crear una instancia EC2 con UserData
1. Escriba un script que cree una instancia EC2 con un UserData que:
    - Instale el paquete de apache (httpd).
    - Inicialize el servicio.

## Ejercicio 8: Crear un Security Group permitiendo trafico web
1. Escriba un script que cree un SG que permita el trafico web desde cualquier direccion IP (0.0.0.0/0)
2. Asocie este security group a la instancia creada anteriormente.
3. Navegue a la ip publica de la instancia para confirmar que el servicio se esta exponiendo correctamente.

### Opcional

Genere un archivo index.html e instalelo en el DocumentRoot de apache para mostrar un contenido distinto al default

## Ejercicio 9: Crear una Base MySQL en RDS 

1. Escriba un script que cree una base de datos con el motor MySQL
2. El usuario debera llamarse admin
3. La password **NO** debera estar directamente en el codigo

