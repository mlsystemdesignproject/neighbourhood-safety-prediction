import boto3
from botocore.exceptions import ClientError


session = boto3.session.Session()
s3 = session.client(service_name="s3", endpoint_url="https://storage.yandexcloud.net")

print("In s3-neighbourhood-safety we have:")
for key in s3.list_objects(Bucket="s3-neighbourhood-safety")["Contents"]:
    print(key["Key"])

try:
    s3.download_file(
        "s3-neighbourhood-safety",
        "alex-test/test_file.txt",
        "scripts/s3_examples/data/downloaded_file.txt",
    )
except ClientError as e:
    print(e)
