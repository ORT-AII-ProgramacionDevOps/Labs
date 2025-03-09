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

5. Instala una distribución de Linux desde Microsoft Store (por ejemplo, Ubuntu).

6. Una vez instalada, abre la distribución desde el menú de inicio y sigue las instrucciones de configuración.

## Ejercicios Git

Para ver los ejercicios de Git, consulta el archivo [Ejercicios Git](./Ejercicios/Git/Ejercicios.md).

## Ejercicios Boto3

Para ver los ejercicios de Boto3, consulta el archivo [Ejercicios Boto3](./Ejercicios/boto3/Ejercicios.md).