# Pulumi + Localstack + Python

This repo demonstrates use of Pulumi with Localstack. 

Following AWS services have been used:
- Kinesis
- IAM
- Lambda
- Dynamodb

Python used as a language to configure Pulumi and to defined example Lambda.

# Prerequisites

## Python

Follow this instructions https://www.python.org/downloads/

**NOTE** Python 3.9 was used in this project

## AWS CLI

Follow this instructions https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html 

## Docker

Follow this instructions https://docs.docker.com/get-docker/

## Localstack

To get `localstack` running, clone this repo: https://github.com/localstack/localstack

Once you have repo cloned, start it with command (from inside of the cloned repo folder):

```shell
docker-compose up --detach
```

**NOTE** to stop `localstack`, use following command:
```shell
docker-compose down
```

You will need to create a AIM user `default_user`, you can do it using this command:

```shell
aws --endpoint-url=http://localhost:4566 iam create-user --user-name default_user
```

## Pulumi

Follow this instructions https://www.pulumi.com/docs/get-started/install/

Once you have Pulumi installed, run following script:

```shell
./scripts/pulumi-setup.sh
```

## How to run it

With `localstack` docker compose up and running

1. Activate `venv`

```shell
cd project
source ./venv/bin/activate
```

2. Bring  pulumi stack up

```shell
pulumi up
```