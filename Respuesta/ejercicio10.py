import boto3
import time

# Crear cliente de CloudWatch Logs
client = boto3.client('logs')

# Nombre del Log Group y Log Stream
log_group_name = 'mi-log-group'
log_stream_name = 'mi-log-stream'

# Crear Log Group
client.create_log_group(logGroupName=log_group_name)

# Crear Log Stream
client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)

# Enviar mensaje de prueba al Log Stream
response = client.put_log_events(
    logGroupName=log_group_name,
    logStreamName=log_stream_name,
    logEvents=[
        {
            'timestamp': int(round(time.time() * 1000)),
            'message': 'Este es un mensaje de prueba'
        },
    ],
)

print("Log Group y Log Stream creados, y mensaje de prueba enviado.")