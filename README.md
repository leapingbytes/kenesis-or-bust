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
./script/iam-create-default-user.sh
```

## Pulumi

Follow this instructions https://www.pulumi.com/docs/get-started/install/

Once you have Pulumi installed, run following script:

```shell
./scripts/pulumi-setup.sh
```

## How to run it

With `localstack` docker compose up and running

1. Prepare lambda archive

Run this script:

```shell
./scripts/prepare-lambda.sh
```

2. Activate `venv`

```shell
cd project
source ./venv/bin/activate
```

3. Bring  pulumi stack up

```shell
export PULUMI_HOME=$(pwd)
export PULUMI_CONFIG_PASSPHRASE=local
pulumi up
```

4. Put records in Kinesis

You can use this script to put data in kinesis

```shell
./script/kinesis-put-record.sh <data string>
```

for example:

```shell
./script/kinesis-put-record.sh "Hello World of Localstack"
```

5. Inspect content of the Dynamodb

## Cleanup

```shell
pulumi destroy
```

You can use this script to see content of the DynamoDB

```shell
./script/kinesis-scan.sh 
```

You should see one record for each time you used `kinesis-put-record.sh`

