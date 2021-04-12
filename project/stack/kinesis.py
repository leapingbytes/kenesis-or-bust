import pulumi as p
import pulumi_aws as p_aws


def define_kinesis_stream(aws_provider: p_aws.Provider):

    kinesis_config = p.Config('kinesis')

    stream = p_aws.kinesis.Stream(
        kinesis_config.get('streamName'),
        name=kinesis_config.get('streamName'),
        shard_count=kinesis_config.get_int('shardCount'),
        opts=p.ResourceOptions(provider=aws_provider),
    )

    p.export('kinesis', stream.arn)

    return stream
