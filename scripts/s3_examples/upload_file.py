import boto3
from botocore.exceptions import ClientError


session = boto3.session.Session()
s3 = session.client(service_name="s3", endpoint_url="https://storage.yandexcloud.net")


try:
    response = s3.upload_file(
        "scripts/s3_examples/data/test_file_to_upload.txt",
        "s3-neighbourhood-safety",
        "alex-test/test_file.txt",
        ExtraArgs={"ACL": "public-read"},
    )
except ClientError as e:
    print(e)

print("Now in s3-neighbourhood-safety we have:")
for key in s3.list_objects(Bucket="s3-neighbourhood-safety")["Contents"]:
    print(key["Key"])
