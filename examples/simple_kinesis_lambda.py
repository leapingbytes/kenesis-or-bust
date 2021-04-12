from __future__ import print_function
import os
import base64
import uuid

import boto3


def lambda_handler(event, context):
    #
    # Boto does not want to work without this :(
    #
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"

    #
    # localstack lambda uses docker as a "executor", so
    # `host.docker.internal` refer to host `localhost`
    #
    dynamodb_client = boto3.client('dynamodb', endpoint_url='http://host.docker.internal:4566')

    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        print("Decoded payload: " + str(payload))

        dynamodb_client.put_item(
            Item={
                "data": {
                    "S": str(payload)
                },
                "id": {
                    "S": str(uuid.uuid4())
                }
            },
            TableName='simple-table'
        )

