import json
import os


def parse_event_payload(event):
    if isinstance(event, dict) and "body" in event:
        body = event.get("body") or "{}"
        if event.get("isBase64Encoded"):
            raise ValueError("No se soporta body en base64 en este ejemplo")
        if isinstance(body, str):
            return json.loads(body)
        if isinstance(body, dict):
            return body
        return {}
    return event or {}


def lambda_handler(event, context):
    try:
        payload = parse_event_payload(event)
        nombre = payload.get("nombre", "mundo")
        accion = payload.get("accion", "saludar")
        cantidad = int(payload.get("cantidad", 1))
    except (ValueError, TypeError, json.JSONDecodeError) as exc:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "error": "payload_invalido",
                    "detalle": str(exc),
                },
                ensure_ascii=False,
            ),
        }

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
