#!/bin/bash

if [ -d ./state ]
then
  echo "STATE already exists"
else
  mkdir ./state
  pulumi login file://$(pwd)/state
fi

if [ -d ./project/venv ]
then
  echo "VENV already exists"
else
  cd project
  python3 -m venv venv
  . ./venv/bin/activate
  pip install -r requirements.txt
  deactivate
fi

if [ -d ./state/.pulumi/stacks/local.json ]
then
  echo "STACK local already exists"
else
  . ./venv/bin/activate
  pulumi stack init --stack local
fi
