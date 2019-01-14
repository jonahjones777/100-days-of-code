npx aws-api-gateway-cli-test \ 
--username='jonah.jones@maine.edu' \ 
--password='Password!23' \ 
--user-pool-id='us-east-1_iNWHG3L55' \ 
--app-client-id='4huesviidiq37r02r388j9rm9f' \ 
--cognito-region='us-east-1' \ 
--identity-pool-id='us-east-1:94b6c2c3-768a-4acb-aee8-fe974a6b7bad' \ 
--invoke-url='https://1ii5lfc5qd.execute-api.us-east-1.amazonaws.com/dev' \ 
--api-gateway-region='us-east-1' \ 
--path-template='/notes
' \ 
--body='{'content': 'hello world', 'attachment': 'hello.jpg'}' \ 
