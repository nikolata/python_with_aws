#!/bin/bash 
echo Please enter a valid IP address:
read ip_address
echo IP address:$ip_address
# bucket=`aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d ',' | sed -e 's/"//g' | xargs`
bucket="nm-2020-10-01-s3site"

# echo export bucket=`aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d ',' | sed -e 's/"//g' | xargs` >> /home/nikola/python_aws/.bashrc
echo export bucket="nm-2020-10-01-s3site" >> /home/nikola/python_aws/.bashrc
echo export bucket_url="https://${bucket}.s3-us-east-2.amazonaws.com/index.html" >> /home/nikola/python_aws/.bashrc
echo BUCKEETTTTT ${bucket}
FILE_PATH="/home/nikola/python_aws/resources/public_policy.json"
FILE_PATH_2="/home/nikola/python_aws/resources/permissions.py"
aws s3 cp --cache-control max-age=0 --content-type image/jpg ~/python_aws/resources/website/backdrop_camera.jpg s3://$bucket/backdrop_camera.jpg 
aws s3 cp --cache-control max-age=0 --content-type text/html ~/python_aws/resources/website/callback.html s3://$bucket/callback.html
aws s3 cp --cache-control max-age=0 --content-type application/javascript ~/python_aws/resources/website/config.js s3://$bucket/config.js
aws s3 cp --cache-control max-age=0 --content-type text/css ~/python_aws/resources/website/core.css s3://$bucket/core.css
aws s3 cp --cache-control max-age=0 --content-type application/javascript ~/python_aws/resources/website/flex_search.js s3://$bucket/flex_search.js
aws s3 cp --cache-control max-age=0 --content-type text/html ~/python_aws/resources/website/index.html s3://$bucket/index.html
aws s3 cp --cache-control max-age=0 --content-type application/javascript ~/python_aws/resources/website/jquery.js s3://$bucket/jquery.js
aws s3 cp --cache-control max-age=0 --content-type image/png ~/python_aws/resources/website/kiosk.png s3://$bucket/kiosk.png
aws s3 cp --cache-control max-age=0 --content-type image/png ~/python_aws/resources/website/kiosk_bottom.png s3://$bucket/kiosk_bottom.png
aws s3 cp --cache-control max-age=0 --content-type image/png ~/python_aws/resources/website/kiosk_left.png s3://$bucket/kiosk_left.png
aws s3 cp --cache-control max-age=0 --content-type image/png ~/python_aws/resources/website/kiosk_right.png s3://$bucket/kiosk_right.png
aws s3 cp --cache-control max-age=0 --content-type image/png ~/python_aws/resources/website/kiosk_top.png s3://$bucket/kiosk_top.png
aws s3 cp --cache-control max-age=0 --content-type text/css ~/python_aws/resources/website/main.css s3://$bucket/main.css
aws s3 cp --cache-control max-age=0 --content-type application/javascript ~/python_aws/resources/website/main.js s3://$bucket/main.js
aws s3 cp --cache-control max-age=0 --content-type application/javascript ~/python_aws/resources/website/products.js s3://$bucket/products.js
aws s3 cp --cache-control max-age=0 --content-type text/html ~/python_aws/resources/website/report.html s3://$bucket/report.html
aws s3 cp --cache-control max-age=0 --content-type text/css ~/python_aws/resources/website/reset.css s3://$bucket/reset.css
aws s3 cp --cache-control max-age=0 --content-type text/css ~/python_aws/resources/website/search.css s3://$bucket/search.css
aws s3 cp --cache-control max-age=0 --content-type application/javascript ~/python_aws/resources/website/search.js s3://$bucket/search.js
sed -i "s/<FMI_1>/$bucket/g" $FILE_PATH
sed -i "s/<FMI_2>/$ip_address/g" $FILE_PATH
sed -i "s/<FMI_3>/$ip_address/g" $FILE_PATH
sed -i "s/<FMI>/$bucket/g" $FILE_PATH_2
python /home/nikola/python_aws/resources/permissions.py