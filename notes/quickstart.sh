#!/bin/bash

# region=us-east-1


# aws cloudformation create-stack \
#     --stack-name notes-backend \
#     --template-url https://s3.amazonaws.com/notes-artifactstores3location-ap8i1gybzyuw/backend.yml \
#     --parameters ParameterKey=S3Artifact,ParameterValue=notes-artifactstores3location-ap8i1gybzyuw \
#     --region $region --capabilities 'CAPABILITY_NAMED_IAM' --output json --profile here

./stackstatus.sh --region us-east-1 --watch --stack-name notes-backend --profile here

# After cloudformation is deployed run the cognito stuff
secs=$((90))
while [ $secs -gt 0 ]; do
   echo -ne "$secs\033[0K\r"
   sleep 1
   : $((secs--))
done

cd .. 
python -u get_cf.py
cd notes-sls
serverless deploy --aws-profile here
