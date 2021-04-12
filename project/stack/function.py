import json

import pulumi as p
import pulumi_aws as p_aws


def define_function(kinesis_arn: str, db_arn: str, aws_provider: p_aws.Provider):

    lambda_config = p.Config('lambda')

    policy = """
    {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }]
    }
    """

    kinesis_lambda_role = p_aws.iam.Role(
        "kinesis-lambda-role",
        assume_role_policy=policy,
        managed_policy_arns=[
            'arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole',
            'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess'
        ],
        opts=p.ResourceOptions(provider=aws_provider)
    )

    p.export('kinesis-lambda-role', kinesis_lambda_role.arn)

    deployment_config = lambda_config.get_object('deployment')

    function = p_aws.lambda_.Function(
        'simple-kinesis-lambda',
        runtime=p_aws.lambda_.Runtime.PYTHON3D8,
        timeout=5,
        handler='simple_kinesis_lambda.lambda_handler',
        role=kinesis_lambda_role.arn,
        code=p.FileArchive(deployment_config['path']),
        opts=p.ResourceOptions(provider=aws_provider)
    )

    p.export('function', function.arn)

    event_source_mapping = p_aws.lambda_.EventSourceMapping(
        'kinesis-event-source-mapping',
        function_name=function.name,
        batch_size=100,
        starting_position='TRIM_HORIZON',
        event_source_arn=kinesis_arn,
        opts=p.ResourceOptions(provider=aws_provider)
    )

    p.export('event_source', event_source_mapping.uuid)
