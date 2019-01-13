AWS_PROFILE=here serverless invoke local --function create --path mocks/create-event.json

AWS_PROFILE=here serverless invoke local --function get --path mocks/get-event.json

AWS_PROFILE=here serverless invoke local --function list --path mocks/list-event.json

AWS_PROFILE=here serverless invoke local --function update --path mocks/update-event.json

AWS_PROFILE=here serverless invoke local --function delete --path mocks/delete-event.json


serverless deploy --aws-profile here
serverless remove --aws-profile here