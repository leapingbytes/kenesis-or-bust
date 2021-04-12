#!/usr/bin/env bash

export DATA=${1:-Hello Kinessis}
export PARTITION_KEY=${2:-$( date +%s )}

aws --endpoint-url=http://localhost:4566 kinesis put-record --stream-name testStream --data $( echo -n $DATA | openssl base64 ) --partition-key 42