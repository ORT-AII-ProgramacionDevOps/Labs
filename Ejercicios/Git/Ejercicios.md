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
2. Modifica exactamente la misma línea del archivo y realiza un commit.

### Paso 3: Volver a `master` y modificar el archivo
1. Cambia de vuelta a la rama `main` o `master`, según corresponda en tu repositorio.
2. Modifica exactamente la misma línea del archivo, pero con otro contenido, y realiza un commit.

### Paso 4: Intentar hacer merge y resolver el conflicto
1. Intenta hacer un merge de la rama `feature` en `main` o `master`.
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
1. Cambia a la rama `main` o `master` y realiza modificaciones sobre la misma línea que cambiaste en `feature`.
2. Empuja los cambios al repositorio remoto.

### Paso 4: Hacer pull de los cambios remotos y resolver el conflicto
1. Cambia a la rama `feature` y haz un pull de los cambios de `main` o `master`.
2. Resuelve el conflicto manualmente editando el archivo.
3. Una vez resuelto, añade los cambios y realiza un commit.
4. Empuja los cambios resueltos al repositorio remoto.

## Ejercicio 9: Forzar un conflicto de merge de forma guiada e interactiva

### Objetivo
1. Generar un conflicto real y repetible entre dos ramas modificando la misma línea de un archivo.
2. Observar el estado del repositorio antes, durante y después de resolver el conflicto.

### Paso 1: Crear el repositorio de prueba
1. Inicializa un repositorio nuevo.
2. Crea un archivo llamado `app.txt` con este contenido:
   - `color=azul`
   - `puerto=8080`
3. Realiza un commit inicial.

### Paso 2: Crear una rama y cambiar una línea
1. Crea la rama `feature-login` y cámbiate a ella.
2. Cambia la línea `color=azul` por `color=verde`.
3. Realiza un commit.

### Paso 3: Volver a la rama principal y generar el conflicto
1. Vuelve a `main` o `master`.
2. Cambia la misma línea `color=azul` por `color=rojo`.
3. Realiza un commit.

### Paso 4: Ejecutar el merge y analizar el conflicto
1. Ejecuta el merge de `feature-login` sobre la rama actual.
2. Ejecuta `git status`.
3. Abre el archivo y analiza las marcas `<<<<<<<`, `=======` y `>>>>>>>`.

### Paso 5: Resolver el conflicto manualmente
1. Edita el archivo dejando un único valor final para la línea `color=`.
2. Agrega el archivo resuelto.
3. Realiza el commit de merge.

### Paso 6: Hacerlo interactivo en clase
1. Un alumno puede trabajar en la rama `feature-login` y otro en `main`.
2. Antes del merge, pídeles que anticipen si Git podrá unir los cambios automáticamente o no.
3. Durante el conflicto, pídeles que expliquen qué representa cada bloque dentro del archivo.
4. Después de resolverlo, comparen el historial con `git log --oneline --graph --all`.
