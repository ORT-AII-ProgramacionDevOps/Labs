import boto3

logs=boto3.client('logs')

logs.create_log_group(logGroupName='test-log-group')
logs.create_log_stream(logGroupName='test-log-group', logStreamName='my-log-stream')