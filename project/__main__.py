# Uncomment to debug in IntelliJ
# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=8800, stdoutToServer=True, stderrToServer=True)

import pulumi as p

from local.local_k8 import get_k8_provider as get_local_k8_provider
from local.local_aws import get_aws_provider as get_local_aws_provider

from real.real_k8 import get_k8_provider as get_real_k8_provider
from real.real_aws import get_aws_provider as get_real_aws_provider

from stack.stack import define_stack

k8s_config = p.Config('kubernetes')
aws_config = p.Config('aws')

k8_provider = get_local_k8_provider() if k8s_config.get_bool('isLocal') else get_real_k8_provider()

aws_provider = get_local_aws_provider(k8_provider) if aws_config.get_bool('isLocal') else get_real_aws_provider()

define_stack(k8_provider, aws_provider)

