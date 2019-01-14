AWS_PROFILE=here serverless invoke local --function create --path mocks/create-event.json

AWS_PROFILE=here serverless invoke local --function get --path mocks/get-event.json

AWS_PROFILE=here serverless invoke local --function list --path mocks/list-event.json

AWS_PROFILE=here serverless invoke local --function update --path mocks/update-event.json

AWS_PROFILE=here serverless invoke local --function delete --path mocks/delete-event.json


serverless deploy --aws-profile here
serverless remove --aws-profile here



npx aws-api-gateway-cli-test \
--username='jonah.jones@maine.edu' \
--password='Password!23' \
--user-pool-id='us-east-1_iNWHG3L55 \
--app-client-id='4huesviidiq37r02r388j9rm9f' \
--cognito-region='us-east-1' \
--identity-pool-id='us-east-1:94b6c2c3-768a-4acb-aee8-fe974a6b7bad' \
--invoke-url='YOUR_API_GATEWAY_URL' \
--api-gateway-region='YOUR_API_GATEWAY_REGION' \
--path-template='/notes' \
--method='POST' \
--body='{"content":"hello world","attachment":"hello.jpg"}'