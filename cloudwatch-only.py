import boto3
import time

logs=boto3.client('logs')

logs.create_log_group(logGroupName='test-log-group')
logs.create_log_stream(logGroupName='test-log-group', logStreamName='my-log-stream')

current_time = int(time.time() * 1000)

logs.put_log_events(logGroupName='test-log-group', logStreamName='my-log-stream', logEvents=[{'timestamp': current_time, 'message': 'test log message'}])