#!/bin/sh

cd $1
. easy_rsa/vars-admin
export COMMON_NAME="$2"
sh easy_rsa/build-key $2