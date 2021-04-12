from typing import Optional

import pulumi_kubernetes as kubernetes
from pulumi import ComponentResource, ResourceOptions
from pulumi_kubernetes import Provider

Service = kubernetes.core.v1.Service
ObjectMetaArgs = kubernetes.meta.v1.ObjectMetaArgs
ServiceSpecArgs = kubernetes.core.v1.ServiceSpecArgs
ServicePortArgs = kubernetes.core.v1.ServicePortArgs

Deployment = kubernetes.apps.v1.Deployment
DeploymentSpecArgs = kubernetes.apps.v1.DeploymentSpecArgs
LabelSelectorArgs = kubernetes.meta.v1.LabelSelectorArgs
PodTemplateSpecArgs = kubernetes.core.v1.PodTemplateSpecArgs
PodSpecArgs = kubernetes.core.v1.PodSpecArgs
VolumeArgs = kubernetes.core.v1.VolumeArgs
ContainerArgs = kubernetes.core.v1.ContainerArgs
ContainerPortArgs = kubernetes.core.v1.ContainerPortArgs
EnvVarArgs = kubernetes.core.v1.EnvVarArgs


class LocalStack(ComponentResource):

    def __init__(self, name: str, provider: Provider, opts: Optional[ResourceOptions] = None):
        super().__init__('project:infrastructure:LocalStack', name, opts=opts)

        app_name = "%s-localstack" % name
        app_labels = {'app': app_name}

        localstack_port = 4566

        local_stack_deployment = Deployment(
            app_name,
            metadata=ObjectMetaArgs(
                namespace="default",
            ),
            spec=DeploymentSpecArgs(
                replicas=1,
                selector=LabelSelectorArgs(
                    match_labels=app_labels
                ),
                template=PodTemplateSpecArgs(
                    metadata=ObjectMetaArgs(
                        labels=app_labels
                    ),
                    spec=PodSpecArgs(
                        containers=[
                            ContainerArgs(
                                name=app_name,
                                image='localstack/localstack',
                                ports=[
                                    ContainerPortArgs(
                                        name="port-%i" % localstack_port, container_port=localstack_port,
                                        host_port=localstack_port)],
                                env=[
                                    EnvVarArgs(
                                        name='SERVICES',
                                        value='apigateway,lambda,iam,sts,s3,dynamodb,kinesis,redshift,stepfunctions'
                                        # TODO
                                    ),
                                    EnvVarArgs(
                                        name='LAMBDA_EXECUTOR',
                                        value='docker-reuse'
                                    ),
                                    EnvVarArgs(
                                        name='PORT_WEB_UI',
                                        value='8080'
                                    ),
                                ]
                            )
                        ]
                    )
                )
            ),
            opts=ResourceOptions(parent=self, provider=provider),
        )

        Service(
            app_name,
            metadata=ObjectMetaArgs(
                name="localstack",
                labels=local_stack_deployment.metadata['labels'],
                namespace="default",
            ),
            spec=ServiceSpecArgs(
                external_traffic_policy='Cluster',
                type='LoadBalancer',
                selector=app_labels,
                ports=[ServicePortArgs(
                    name="port-%i" % localstack_port, port=localstack_port,
                    target_port=localstack_port)]
            ),
            opts=ResourceOptions(parent=self, provider=provider),
        )
