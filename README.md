# Pulumi/CDK + Localstack + Python

**TOC**
- [Prerequisites](#prerequisites)
- [How To Run Pulumi](#how-to-run-pulumi)
- [Hot to run CDK](#how-to-run-cdk)

This repo demonstrates use of Pulumi & CDK with Localstack. 

Following AWS services have been used:
- Kinesis
- IAM
- Lambda
- Dynamodb

Python used as a language to configure Pulumi & CDK and to defined example Lambda.

# Prerequisites

## Python

Follow this instructions https://www.python.org/downloads/

**NOTE** Python 3.9 was used in this project

## AWS CLI(local)

Follow this instructions [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html ](https://github.com/localstack/awscli-local)

## CDK(loal)

Follow this instructions [https://www.npmjs.com/package/aws-cdk-local](https://www.npmjs.com/package/aws-cdk-local)

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
export PULUMI_HOME=$(pwd)
export PULUMI_CONFIG_PASSPHRASE=local
./scripts/pulumi-setup.sh
```

## How to run Pulumi

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

You can use this script to see content of the DynamoDB

```shell
./script/kinesis-scan.sh 
```

You should see one record for each time you used `kinesis-put-record.sh`

## Cleanup

```shell
pulumi destroy
```

## How to Run CDK

1. Prepare lambda archive

Run this script:

```shell
./scripts/prepare-lambda.sh
```
2. Create `.venv`

```
cd cdk
python3 -m venv .venv
```

3. Activate `.venv` and install dependencies

```
. ./.venv/bin/activate

pip install -r requirements.txt
```

4. Prepare CDK asset management stack

```
cdklocal bootstrap aws://unknown-account/eu-central-1
```

5. Deploy CDK stack

```
cdklocal deploy
```

6. Put records in Kinesis

You can use this script to put data in kinesis

```shell
./script/kinesis-put-record.sh <data string>
```

for example:

```shell
./script/kinesis-put-record.sh "Hello World of Localstack"
```

7. Inspect content of the Dynamodb

You can use this script to see content of the DynamoDB

```shell
./script/kinesis-scan.sh 
```

## Cleanup

```shell
cdk destroy
```