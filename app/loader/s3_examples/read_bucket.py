import boto3

session = boto3.session.Session()
s3 = session.client(service_name="s3", endpoint_url="https://storage.yandexcloud.net")
response = s3.list_buckets()

print("In this account, we can read these buckets.")
for bucket in response["Buckets"]:
    print(f'- {bucket["Name"]}')

print("In s3-neighbourhood-safety we have files")
for key in s3.list_objects(Bucket="s3-neighbourhood-safety")["Contents"]:
    print(key["Key"])
