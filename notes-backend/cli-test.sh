#!/bin/bash 
npx aws-api-gateway-cli-test \
--username 'jonah.jones@maine.edu' \
--password 'Password!23' \
--user-pool-id 'us-east-1_4LQCi2FeJ' \
--app-client-id '6t0c83eplce1pd4t2alpvlu6f9' \
--cognito-region 'us-east-1' \
--identity-pool-id 'us-east-1:458b4175-adcf-4a54-9dff-0bb6546d2384' \
--invoke-url 'https://1ii5lfc5qd.execute-api.us-east-1.amazonaws.com/dev' \
--api-gateway-region 'us-east-1' \
--path-template '/notes' \
--method 'POST' \
--body '{"content":"hello world","attachment":"hello.jpg"}' \
