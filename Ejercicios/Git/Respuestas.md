# Respuestas a Ejercicios Básicos de Git

## Ejercicio 1: Configuración Inicial
1. Configura tu nombre de usuario.
   
    ```sh
    git config --global user.name "Tu Nombre"
    ```
2. Configura tu correo electrónico.
   
    ```sh
    git config --global user.email "tuemail@example.com"
    ```

## Ejercicio 2: Crear Repositorio y clonar repositorio
1. Crea un repositorio en GitHub.
2. Clona el repositorio en tu máquina local.
   
    ```sh
    git clone https://github.com/usuario/repositorio.git
    ```

## Ejercicio 3: Crear Rama llamada bash
1. Crea una rama llamada `bash`.
   
    ```sh
    git branch bash
    ```
2. Cambia a la rama `bash`.
   
    ```sh
    git checkout bash
    ```

## Ejercicio 4: Commitear los scripts y subirlos a nuestro repositorio local
1. Genera un commit con un mensaje que diga "Subida de scripts de bash".
   
    ```sh
    git add .
    git commit -m "Subida de scripts de bash"
    ```

## Ejercicio 5: Realice un Merge de la rama bash a la rama main 
1. Cambia a la rama `main`.
   
    ```sh
    git checkout main
    ```
2. Realiza el merge de la rama `bash` a la rama `main`.
   
    ```sh
    git merge bash
    ```
## Ejercicio 6: Pushe los cambios hacia el repositorio remoto
   
    git push


## Ejercicio 7: Resolver Conflictos de Ramas (Local)

### Paso 1: Crear el repositorio
1. Inicializa un nuevo repositorio local.
    ```sh
    git init
    ```
2. Crea un archivo inicial y realiza un commit.
    ```sh
    echo "Contenido inicial" > archivo.txt
    git add archivo.txt
    git commit -m "Commit inicial"
    ```
### Paso 2: Crear la rama `feature` y modificar el archivo
1. Crea una nueva rama llamada `feature` y cámbiate a ella.
    ```sh
    git branch feature
    git checkout feature
    ```
2. Modifica el archivo y realiza un commit.
    ```sh
    echo "Cambio en feature" >> archivo.txt
    git add archivo.txt
    git commit -m "Modificación en feature"
    ```
### Paso 3: Volver a `master` y modificar el archivo
1. Cambia de vuelta a la rama `master`.
    ```sh
    git checkout master
    ```
2. Modifica el archivo y realiza un commit.
    ```sh
    echo "Cambio en master" >> archivo.txt
    git add archivo.txt
    git commit -m "Modificación en master"
    ```
### Paso 4: Intentar hacer merge y resolver el conflicto
1. Intenta hacer un merge de la rama `feature` en `master`.
    ```sh
    git merge feature
    ```
2. Resuelve el conflicto manualmente editando el archivo.
3. Una vez resuelto, añade los cambios y realiza un commit.
    ```sh
    git add archivo.txt
    git commit -m "Conflicto resuelto entre master y feature"
    ```

## Ejercicio 8: Resolver Conflictos de Ramas (Remoto)

### Paso 1: Clonar el repositorio remoto
1. Clona el repositorio remoto.
    ```sh
    git clone https://github.com/usuario/repositorio.git
    cd repositorio
    ```
### Paso 2: Crear y trabajar en la rama `feature`
1. Crea una nueva rama llamada `feature` y cámbiate a ella.
    ```sh
    git branch feature
    git checkout feature
    ```
2. Modifica un archivo y realiza un commit.
    ```sh
    echo "Cambio en feature" >> archivo.txt
    git add archivo.txt
    git commit -m "Modificación en feature"
    ```
3. Empuja los cambios al repositorio remoto.
    ```sh
    git push -u origin feature
    ```
### Paso 3: Simular cambios en la rama `master` (en el remoto)
1. Cambia a la rama `master`.
    ```sh
    git checkout master
    ```
2. Realiza modificaciones en el archivo y realiza un commit.
    ```sh
    echo "Cambio en master" >> archivo.txt
    git add archivo.txt
    git commit -m "Modificación en master"
    ```
3. Empuja los cambios al repositorio remoto.
    ```sh
    git push
    ```
### Paso 4: Hacer pull de los cambios remotos y resolver el conflicto
1. Cambia a la rama `feature` y haz un pull de los cambios de `master`.
    ```sh
    git checkout feature
    git pull origin master
    ```
2. Resuelve el conflicto manualmente editando el archivo.
3. Una vez resuelto, añade los cambios y realiza un commit.
    ```sh
    git add archivo.txt
    git commit -m "Conflicto resuelto entre master y feature"
    ```
4. Empuja los cambios resueltos al repositorio remoto.
    ```sh
    git push
    ```