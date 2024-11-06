import boto3

s3=boto3.client('s3')


s3.create_bucket(Bucket='312jr23ifjsdio')

s3.upload_file('userdata.sh', '312jr23ifjsdio', 'script-de-userdata')