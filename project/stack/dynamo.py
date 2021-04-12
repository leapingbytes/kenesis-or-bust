import pulumi as p
import pulumi_aws as p_aws


def define_dynamo_db(aws_provider: p_aws.Provider):
    table = p_aws.dynamodb.Table(
        'simple-table',
        name='simple-table',
        attributes=[
            p_aws.dynamodb.TableAttributeArgs(
                name="id",
                type="S",
            )
        ],
        billing_mode='PROVISIONED',
        hash_key='id',
        read_capacity=10,
        write_capacity=10,
        opts=p.ResourceOptions(provider=aws_provider),
    )

    p.export('table', table.arn)

    return table
