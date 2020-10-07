import boto3
import subprocess 

# bucket_name_str = subprocess.getoutput('aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d "," | xargs')
bucket_name_str = "nm-2020-10-01-s3site"
client = boto3.client('apigateway', region_name='us-east-2')
client_bucket = boto3.client('s3', region_name='us-east-2')
bucket = client_bucket.list_buckets()
# print(bucket_name_str)
response = client.get_rest_apis(
    limit=10
)

ID = response['items'][0]['id']
resources = client.get_resources(restApiId=ID)

create_report_id = [resource for resource in resources["items"] if resource["path"] == "/create_report"][0]["id"]
#print (create_report_id)
get_reviews_id = [resource for resource in resources["items"] if resource["path"] == "/get_reviews"][0]["id"]
#print (get_reviews_id) 
get_av_star_rating_id = [resource for resource in resources["items"] if resource["path"] == "/get_av_star_rating"][0]["id"]
#print (get_av_star_rating_id)

#options_method1 = client.put_method(
#    restApiId=ID,
#    resourceId=get_reviews_id,
#    httpMethod='OPTIONS',
#    authorizationType='NONE'
#
#)

#options_method2 = client.put_method(
#    restApiId=ID,
#    resourceId=get_av_star_rating_id,
#    httpMethod='OPTIONS',
#    authorizationType='NONE'
#
#)

options_method = client.put_method(
    restApiId=ID,
    resourceId=create_report_id,
    httpMethod='OPTIONS',
    authorizationType='NONE'

)

#options_mock1 = client.put_integration(
#    restApiId=ID,
#    resourceId=get_reviews_id,
#    httpMethod='OPTIONS',
#    type='MOCK',
#    requestTemplates={
#        'application/json': '{"statusCode": 200}'
#    }
#)

#options_mock2 = client.put_integration(
#    restApiId=ID,
#    resourceId=get_av_star_rating_id,
#    httpMethod='OPTIONS',
#    type='MOCK',
#    requestTemplates={
#        'application/json': '{"statusCode": 200}'
#    }
#)

options_mock = client.put_integration(
    restApiId=ID,
    resourceId=create_report_id,
    httpMethod='OPTIONS',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)

options_method_response = client.put_method_response(
    restApiId=ID,
    resourceId=create_report_id,
    httpMethod='OPTIONS',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True,
        'method.response.header.Access-Control-Allow-Credentials': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

#options_method_response2 = client.put_method_response(
#    restApiId=ID,
#    resourceId=get_reviews_id,
#    httpMethod='OPTIONS',
#    statusCode='200',
#    responseParameters={
#        'method.response.header.Access-Control-Allow-Headers': False,
#        'method.response.header.Access-Control-Allow-Origin': False,
#        'method.response.header.Access-Control-Allow-Methods': False
#    },
#    responseModels={
#        'application/json': 'Empty'
#    }
#)

#options_method_response3 = client.put_method_response(
#    restApiId=ID,
#    resourceId=get_av_star_rating_id,
#    httpMethod='OPTIONS',
#    statusCode='200',
#    responseParameters={
#        'method.response.header.Access-Control-Allow-Headers': False,
#        'method.response.header.Access-Control-Allow-Origin': False,
#        'method.response.header.Access-Control-Allow-Methods': False
#    },
#    responseModels={
#        'application/json': 'Empty'
#    }
#)

options_integration_response = client.put_integration_response(
    restApiId=ID,
    resourceId=create_report_id,
    httpMethod='OPTIONS',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'POST,OPTIONS\'',
        'method.response.header.Access-Control-Allow-Origin': "'https://" + bucket_name_str + ".s3-us-east-2.amazonaws.com'",
        'method.response.header.Access-Control-Allow-Credentials': "'true'"

    },
    responseTemplates={
        'application/json': ''
    }
)

#options_integration_response2 = client.put_integration_response(
#    restApiId=ID,
#    resourceId=get_reviews_id,
#    httpMethod='OPTIONS',
#    statusCode='200',
#    responseParameters={
#        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
#        'method.response.header.Access-Control-Allow-Methods': '\'POST,OPTIONS\'',
#        'method.response.header.Access-Control-Allow-Origin': '\'*\''
#    },
#    responseTemplates={
#        'application/json': ''
#    }
#)

#options_integration_response3 = client.put_integration_response(
#    restApiId=ID,
#    resourceId=get_av_star_rating_id,
#    httpMethod='OPTIONS',
#    statusCode='200',
#    responseParameters={
#        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
#       'method.response.header.Access-Control-Allow-Methods': '\'POST,OPTIONS\'',
#        'method.response.header.Access-Control-Allow-Origin': '\'*\''
#    },
#    responseTemplates={
#        'application/json': ''
#    }
#)

print("DONE")
