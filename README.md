## Cómo instalar WSL

1. Abre PowerShell como administrador y ejecuta el siguiente comando para habilitar WSL:
    ```sh
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
2. Habilita la característica de máquina virtual:
    ```sh
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```

## Instalación de WSL y una distribución de Linux
1. Alternativamente, puedes instalar WSL y una distribución de Linux con un solo comando:
    ```sh
    wsl --install
    ```

2. Por defecto, al utilizar el comando:
    ```sh
    wsl --install
    ```
    se instala Ubuntu como distribución predeterminada.

3. Una vez instalada, abre la distribución desde el menú de inicio y sigue las instrucciones de configuración.

4. Es probable que tengas que reiniciar el equipo para poder utilizar WSL 

## Cómo instalar Git

### En Windows

1. Descarga el instalador de Git desde el [sitio oficial](https://git-scm.com/download/win).

2. Ejecuta el instalador y sigue las instrucciones del asistente de instalación.

3. Una vez completada la instalación, abre una terminal y verifica la instalación con el siguiente comando:
    ```sh
    git --version
    ```

### En Linux

1. Abre una terminal.

2. Ejecuta el siguiente comando para instalar Git usando el gestor de paquetes de tu distribución (por ejemplo, `apt` para Debian/Ubuntu o `yum` para CentOS):
    ```sh
    sudo apt-get install git
    ```
    o
    ```sh
    sudo yum install git
    ```

3. Verifica la instalación con el siguiente comando:
    ```sh
    git --version
    ```

## Ejercicios Git

Para ver los ejercicios de Git, consulta el archivo [Ejercicios Git](./Ejercicios/Git/Ejercicios.md).

## Ejercicios Boto3

Para ver los ejercicios de Boto3, consulta el archivo [Ejercicios Boto3](./Ejercicios/boto3/Ejercicios.md).