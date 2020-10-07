import boto3

client = boto3.client('apigateway', region_name='us-east-2')

response = client.create_rest_api(
    name='Fancy-Api',
    description='test api',
    minimumCompressionSize=123,
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    }
)
api_id = response["id"]

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]

get_reviews = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='get_reviews'
)
get_reviews_id = get_reviews["id"]

get_av_star_rating = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='get_av_star_rating'
)
get_av_star_rating_id = get_av_star_rating["id"]

create_report = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='create_report'
)
create_report_id = create_report["id"]

post_method = client.put_method(
    restApiId=api_id,
    resourceId=create_report_id,
    httpMethod='POST',
    authorizationType='NONE'

)

get_method = client.put_method(
    restApiId=api_id,
    resourceId=get_reviews_id,
    httpMethod='GET',
    authorizationType='NONE',
    requestParameters={
        'method.request.querystring.product_id': False
    }

)

get_method2 = client.put_method(
    restApiId=api_id,
    resourceId=get_av_star_rating_id,
    httpMethod='GET',
    authorizationType='NONE',
    requestParameters={
        'method.request.querystring.product_id': False
    }

)

post_mock = client.put_integration(
    restApiId=api_id,
    resourceId=create_report_id,
    httpMethod='POST',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)

get_mock = client.put_integration(
    restApiId=api_id,
    resourceId=get_reviews_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)

get_mock2 = client.put_integration(
    restApiId=api_id,
    resourceId=get_av_star_rating_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)

post_method_response = client.put_method_response(
    restApiId=api_id,
    resourceId=create_report_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': False,
        'method.response.header.Access-Control-Allow-Origin': False,
        'method.response.header.Access-Control-Allow-Methods': False
    },
    responseModels={
        'application/json': 'Empty'
    }
)

get_method_response1 = client.put_method_response(
    restApiId=api_id,
    resourceId=get_reviews_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': False,
        'method.response.header.Access-Control-Allow-Origin': False,
        'method.response.header.Access-Control-Allow-Methods': False
    },
    responseModels={
        'application/json': 'Empty'
    }
)

get_method_response2 = client.put_method_response(
    restApiId=api_id,
    resourceId=get_av_star_rating_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': False,
        'method.response.header.Access-Control-Allow-Origin': False,
        'method.response.header.Access-Control-Allow-Methods': False
    },
    responseModels={
        'application/json': 'Empty'
    }
)

post_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=create_report_id,
    httpMethod='POST',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'POST\'',
        'method.response.header.Access-Control-Allow-Origin': '\'*\''
    },
    responseTemplates={
        'application/json': '"message_str": "report requested, check your phone shortly"'
    }
)

get_integration_response1 = client.put_integration_response(
    restApiId=api_id,
    resourceId=get_reviews_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'GET\'',
        'method.response.header.Access-Control-Allow-Origin': '\'*\''
    },
    responseTemplates={
        'application/json': '{"product_id_str": "$input.params("product_id")",",reviews_arr: [{ review_body_str: "Both the dropcam and nest cam have an embarrassingly bad WIFI algorithm when there are multiple access points with the same name (SID) near it.  (I have a tall house and I need multiple WIFI access points)  When you have this situation, the cameras lose connectivity all the time. The obvious workaround is to dedicate a WIFI access point specifically for the Nest Cam, which is annoying.  Why Nest can\'t or won\'t fix this is beyond me.  I know of no other WIFI enabled device that is this dumb about WIFI connectivity.  Until this is fixed it stays a 3" rating_float: 3.25 },{ review_body_str: "It was easy to setup with a small hiccup during the scanning of the barcode on the back.  I still have issues with the software not loading correctly on my phone which customer service has said they are working on fixing.  The app hangs quite often when loading it from a push notification where I either get single spinners or double spinners.<br /><br />I do wish the monthly/yearly fees for video retention were better or there was maybe a network based solution for video storage as I would like to buy more of these and use them as a whole house system but would get quite pricy" rating_float: 2.25 },{ review_body_str: "I\'ve had this device for a few weeks now and I really like it.  It was easy to setup and it\'s easy to use.  I already have a Nest thermostat which I love and I now use the same app (on Android) to manage the camera.  It is really cool to be able to view the camera from my phone wherever I am.  There are some small kinks which seem to need work in the app.  For example, clicking on the notification will open the app and infinitely try to load the image from the camera history.  If you don\'t pay for the history it was just infinitely load... you could wait an hour it will never load an image.  You have to back out of the app and open it again to see the image.  Also, the camera should come with at least one day or a few hours of video history included for free.  It would be great to have the option to cache video history to my own computer or network device.  Without paying the subscription fee you have ZERO video history.  You will get a notification that the camera detected motion.... but you can\'t see it because it\'s usually over before you can open the app.  The camera is pretty much useless without video history... but the prices for history are not cheap.  If you don\'t mind paying a monthly fee... it\'s a great device with excellent build quality and image quality." rating_float: 4.25 },{ review_body_str: "I was hoping to use this for outdoor surveillance.  Proved to be too difficult to isolate zones where breezy plants wouldn\'t trigger unwanted alerts.  On one occasion, I received motion alerts when camera was allegedly off, which made me uncomfortable about when video was/wasn\'t being sent to cloud.  App had a bad habit of turning off my motion zones so my alerts were not useful.  Camera pours off heat.  Seems overall like an unrefined product not on par with the Nest thermostat which I own and like." rating_float: 3.50 }] }'

    }
)

get_integration_response2 = client.put_integration_response(
    restApiId=api_id,
    resourceId=get_av_star_rating_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': '\'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token\'',
        'method.response.header.Access-Control-Allow-Methods': '\'GET\'',
        'method.response.header.Access-Control-Allow-Origin': '\'*\''
    },
    responseTemplates={
        'application/json': '{"product_id_str" : "$input.params("product_id")","average_star_review_float":  "3.25"}'
    }
)

print("DONE")