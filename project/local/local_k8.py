import pulumi_kubernetes as p_k8


def get_k8_provider():
    local_k8_provider = p_k8.Provider(resource_name='k8s', context='docker-desktop')
    return local_k8_provider
