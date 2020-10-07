'''
    You must replace <FMI> with your bucket name
'''
import boto3
import json

S3API = boto3.client("s3", region_name="us-east-2")
bucket_name = "nm-2020-10-01-s3site"

# policy_file = open("/home/ec2-user/environment/website_security_policy.json", "r")

policy_file = open("/home/nikola/python_aws/website_security_policy.json", "r")

S3API.put_bucket_policy(
    Bucket=bucket_name,
    Policy=policy_file.read()
)
print("DONE")
