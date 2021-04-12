import pulumi as p
import pulumi_kubernetes as p_k8s
import pulumi_aws as p_aws

from stack.kinesis import define_kinesis_stream
from stack.dynamo import define_dynamo_db
from stack.function import define_function


def define_stack(k8s: p_k8s.Provider, aws: p_aws.Provider):

    stream = define_kinesis_stream(aws)

    dynamo = define_dynamo_db(aws)

    define_function(stream.arn, dynamo.arn, aws)
