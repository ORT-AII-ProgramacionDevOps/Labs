# Ejercicios Básicos de Git

## Prerequisitos

- Cuenta de Github [GitHub](https://github.com)

## Recursos Adicionales
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## Ejercicio 1: Configuración Inicial
1. Configura tu nombre de usuario.
2. Configura tu correo electrónico.

## Ejercicio 2: Crear Repositorio y clonar repositorio
1. Cree un repositorio en donde se van alojar los ejercicios de la materia
2. Clonar el repositorio en su maquina local


## Ejercicio 3: Crear Rama llamada bash 
1. Cree una rama llamada bash en donde se va a subir los scripts de bash creados hasta ahora en el curso

## Ejercicio 4: Commitear los scripts y subirlos a nuestro repositorio local
1. Genere un commit con un mensaje que diga "Subida de scripts de bash" y subalo a su repositorio local

## Ejercicio 5: Mergear cambios desde la rama bash a la rama main 
1. Realice un merge de la rama bash a la rama main para enviar los cambios pusheados en el ejercicio anterior

## Ejercicio 6: Pushe los cambios hacia el repositorio remoto
1. Envie los cambios realizados en el repositorio local hacia el repositorio remoto mediante un push

## Ejercicio 7: Resolver Conflictos de Ramas (Local)

### Paso 1: Crear el repositorio
1. Inicializa un nuevo repositorio local.
2. Crea un archivo inicial y realiza un commit.

### Paso 2: Crear la rama `feature` y modificar el archivo
1. Crea una nueva rama llamada `feature` y cámbiate a ella.
2. Modifica el archivo y realiza un commit.

### Paso 3: Volver a `master` y modificar el archivo
1. Cambia de vuelta a la rama `master`.
2. Modifica el archivo y realiza un commit.

### Paso 4: Intentar hacer merge y resolver el conflicto
1. Intenta hacer un merge de la rama `feature` en `master`.
2. Resuelve el conflicto manualmente editando el archivo.
3. Una vez resuelto, añade los cambios y realiza un commit.


## Ejercicio 8: Resolver Conflictos de Ramas (Remoto)

### Paso 1: Clonar el repositorio remoto
1. Clona un repositorio remoto:

### Paso 2: Crear y trabajar en la rama `feature`
1. Crea una nueva rama llamada `feature` y cámbiate a ella.
2. Modifica un archivo y realiza un commit.
3. Empuja los cambios al repositorio remoto.

### Paso 3: Simular cambios en la rama `master` (en el remoto)
1. Cambia a la rama `master` y realiza modificaciones.
2. Empuja los cambios al repositorio remoto.

### Paso 4: Hacer pull de los cambios remotos y resolver el conflicto
1. Cambia a la rama `feature` y haz un pull de los cambios de `master`.
2. Resuelve el conflicto manualmente editando el archivo.
3. Una vez resuelto, añade los cambios y realiza un commit.
4. Empuja los cambios resueltos al repositorio remoto.
