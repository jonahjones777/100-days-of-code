#!/bin/bash 
npx aws-api-gateway-cli-test \
--username 'jonah.jones@maine.edu' \
--password 'Password!23' \
--user-pool-id 'us-east-1_ISc2o1ELp' \
--app-client-id '1sid58bocj4jivm5raups65kqk' \
--cognito-region 'us-east-1' \
--identity-pool-id 'us-east-1:c261ab37-e6a5-43d1-ac6b-095890fa0679' \
--invoke-url 'https://1ii5lfc5qd.execute-api.us-east-1.amazonaws.com/dev' \
--api-gateway-region 'us-east-1' \
--path-template '/notes' \
--method 'POST' \
--body '{"content":"hello world","attachment":"hello.jpg"}' \
