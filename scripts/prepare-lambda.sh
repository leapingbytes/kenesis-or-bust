#!/usr/bin/env bash

cd ./examples

if [ ! -d venv ]
then
  python3 -m venv venv
  . ./venv/bin/activate
  pip install boto3
  deactivate
fi

cd venv/lib/python3.9/site-packages

zip -r9 ${OLDPWD}/simple_kinesis_lambda.zip .

cd ${OLDPWD}

zip -g simple_kinesis_lambda.zip simple_kinesis_lambda.py