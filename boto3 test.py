import boto3
s3 = boto3.client('s3', region_name='eu-west-1',)
response = s3.list_buckets()
print(response)
for bucket in response['Buckets']:
    print(bucket['Name'])
response_testBucket = s3.create_bucket(Bucket='my-bucket', 
                                       CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
print(response_testBucket)
response = s3.list_buckets()
response
for bucket in response['Buckets']:
    print(bucket['Name'])