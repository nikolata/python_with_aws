#!/bin/bash
# bucket=`aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d ',' | sed -e 's/"//g' | xargs`
bucket="nm-2020-10-01-s3site"
echo BUCKEETTTTTTTTTTTTTTT: $bucket
aws s3 cp ~/python_aws/resources/website/config.js s3://$bucket/config.js
