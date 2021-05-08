from aws_cdk import ( 
    core as cdk,
    aws_kinesis as kinesis, 
    aws_dynamodb as dynamo,
    aws_lambda_event_sources as events,
    aws_lambda as function,
    aws_logs as logs
)

from aws_cdk import core


class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stream = kinesis.Stream(
            self, 
            'test-stream', 
            stream_name='testStream',
            shard_count=1
        )

        table = dynamo.Table(
            self, 'test-table',       
            table_name='simple-table',     
            partition_key={'name': 'id', 'type': dynamo.AttributeType.STRING},
        )

        stream_event = events.KinesisEventSource(
            stream, 
            starting_position=function.StartingPosition.TRIM_HORIZON
        )

        kinesis_function = function.Function(
            self, 
            'test-function',
            function_name='test-function',
            runtime=function.Runtime.PYTHON_3_7,
            handler='simple_kinesis_lambda.lambda_handler',
            log_retention=logs.RetentionDays.ONE_WEEK,
            memory_size=256,
            timeout=core.Duration.seconds(10),
            tracing=function.Tracing.ACTIVE,
            code=function.Code.from_asset(path='../examples/simple_kinesis_lambda.zip'),
            events=[stream_event]
        )   