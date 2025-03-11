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

## Ejercicio 4: Subir scripts a repositorio remoto
1. Mueve los scripts creados hacia el repositorio clonado.
    ```sh
    mv /ruta/de/scripts/* /ruta/del/repositorio/
    ```
2. Añade los scripts al área de preparación.
    ```sh
    git add .
    ```

## Ejercicio 5: Commitear los scripts y subirlos a nuestro repositorio local
1. Genera un commit con un mensaje que diga "Subida de scripts de bash".
    ```sh
    git commit -m "Subida de scripts de bash"
    ```

## Ejercicio 6: Suba los scripts al repositorio remoto
1. Haz un push con tus cambios al repositorio remoto en GitHub.
    ```sh
    git push origin bash
    ```
