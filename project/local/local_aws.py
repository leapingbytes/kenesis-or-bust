import pulumi_aws as p_aws

# from pulumi import ResourceOptions

from pulumi_kubernetes import Provider

# from local.local_stack import LocalStack


def get_aws_provider(k8_provider: Provider):
    # local_stack = LocalStack("pulumi-aws-localstack", provider=k8_provider)

    local_stack_endpoint = 'http://localhost:4566'

    aws_provider = p_aws.Provider(
        "localstack",
        skip_credentials_validation=True,
        skip_metadata_api_check=True,
        s3_force_path_style=True,
        access_key='mock-access-key',
        secret_key='mock-secret-key',
        region=p_aws.Region.EU_WEST1,
        endpoints=[p_aws.ProviderEndpointArgs(
            apigateway=local_stack_endpoint,
            cloudformation=local_stack_endpoint,
            cloudwatch=local_stack_endpoint,
            cloudwatchlogs=local_stack_endpoint,
            dynamodb=local_stack_endpoint,
            es=local_stack_endpoint,
            firehose=local_stack_endpoint,
            iam=local_stack_endpoint,
            kinesis=local_stack_endpoint,
            kms=local_stack_endpoint,
            lambda_=local_stack_endpoint,
            redshift=local_stack_endpoint,
            route53=local_stack_endpoint,
            stepfunctions=local_stack_endpoint,
            s3=local_stack_endpoint,
            ses=local_stack_endpoint,
            sns=local_stack_endpoint,
            sqs=local_stack_endpoint,
            ssm=local_stack_endpoint,
            sts=local_stack_endpoint,
            # Missing:
            # "DynamoDBStreams": "http://localhost:4570",
            # "Elasticsearch": "http://localhost:4571",
        )]
    )

    return aws_provider
