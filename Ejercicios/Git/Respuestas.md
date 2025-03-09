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

## Ejercicio 2: Realizar un Commit
1. Crea un nuevo archivo y añádele contenido.
    ```sh
    echo "Contenido del archivo" > archivo.txt
    ```
2. Añade el archivo al área de preparación (staging area).
    ```sh
    git add archivo.txt
    ```
3. Realiza un commit con un mensaje descriptivo.
    ```sh
    git commit -m "Añadir archivo.txt con contenido inicial"
    ```

## Ejercicio 3: Ver el Estado del Repositorio
1. Modifica el archivo `hola.txt`.
    ```sh
    echo "Nueva línea" >> hola.txt
    ```
2. Verifica el estado del repositorio.
    ```sh
    git status
    ```

## Ejercicio 4: Ver el Historial de Commits
1. Revisa el historial de commits.
    ```sh
    git log
    ```

## Ejercicio 5: Crear y Cambiar de Rama
1. Crea una nueva rama llamada `nueva-rama`.
    ```sh
    git branch nueva-rama
    ```
2. Cambia a la nueva rama.
    ```sh
    git checkout nueva-rama
    ```

## Ejercicio 6: Fusionar Ramas
1. Cambia de vuelta a la rama principal (`main` o `master`).
    ```sh
    git checkout main
    ```
2. Fusiona la rama `nueva-rama` con la rama principal.
    ```sh
    git merge nueva-rama
    ```

## Ejercicio 7: Clonar un Repositorio
1. Clona un repositorio remoto.
    ```sh
    git clone https://github.com/usuario/repositorio.git
    ```

## Ejercicio 8: Actualizar el Repositorio Local
1. Obtén los últimos cambios del repositorio remoto.
    ```sh
    git pull origin main
    ```

## Ejercicio 9: Enviar Cambios al Repositorio Remoto
1. Envía tus commits al repositorio remoto.
    ```sh
    git push origin main
    ```