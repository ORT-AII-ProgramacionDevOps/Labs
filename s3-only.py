import boto3

s3=boto3.client('s3')

s3.create_bucket(Bucket='dwijdisojdaois')

s3.upload_file('userdata.sh', 'dwijdisojdaois', 'script-de-userdata')