#!/bin/bash

aws cloudformation delete-stack \
    --stack-name notes-backend --region us-east-1 --profile here

# cd ../notes-backend
# serverless remove --aws-profile here
# cd ../notes

./stackstatus.sh --region us-east-1 --watch --stack-name notes-backend --profile here
