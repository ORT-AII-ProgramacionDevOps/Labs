import json
import os


def lambda_handler(event, context):
    nombre = event.get("nombre", "mundo")
    accion = event.get("accion", "saludar")
    cantidad = int(event.get("cantidad", 1))

    ambiente = os.environ.get("APP_ENV", "dev")
    prefijo = os.environ.get("MENSAJE_PREFIJO", "Hola")
    version = os.environ.get("APP_VERSION", "1.0")

    if accion == "despedir":
        mensaje = f"Adios {nombre}"
    else:
        mensaje = f"{prefijo} {nombre}"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "mensaje": mensaje,
                "cantidad": cantidad,
                "parametros_recibidos": {
                    "nombre": nombre,
                    "accion": accion,
                    "cantidad": cantidad,
                },
                "variables_entorno": {
                    "APP_ENV": ambiente,
                    "MENSAJE_PREFIJO": prefijo,
                    "APP_VERSION": version,
                },
            },
            ensure_ascii=False,
        ),
    }
