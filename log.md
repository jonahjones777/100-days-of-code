# 100 Days Of Devops - Log

### Day 1: January 5, 2018

**Today's Progress**: Today I created the cloudformation for my new serverless project deploy pipeline, that included codepipeline, and codebuild. This will kick off froma push to my github repo as well

**Thoughts:** I ran into alot of little syntax errors on the cloudformation, and figuring out the code pipeline/build steps. I think that building the frontend will be a challenge for me, now that I got things done in a logical fashion.

**Link to work:**  TBD

### Day 2: January 6, 2018

**Today's Progress**: Today I created the cloudformation for my new serverless projects backend, that included a dynamodb table, cognito pool, iam role, and custom 2 cloudformation functions to do cognito auth domain, and client settings

**Thoughts:** I ran into a few syntax errors on the cloudformation with items in lists today, also hit a wall with cognito not haviing everything fully supported through cloudformaiton, had to find some custom functions online to handle doing a few items. Creating backend compenents for app today was fun.

**Link to work:**  TBD


### Day 3: January 7, 2018

**Today's Progress**: Today I some scripts to spin up and down and watch the backend cloudformation, and get information from the cognito pools, and create/confirm a fake user using boto3. This will help the initial spin up of the app each day to save costs.

**Thoughts:** I like the idea of spinning up and down this app fully and completly everyday, and only working through python or bash. I think this will not only help save money, but make sure that the code is really done well since I can destroy, and deploy the entire application infrastructure in a matter of minutes at any-point. 

**Link to work:**  TBD

### Day 4: January 8, 2018

**Today's Progress**: Today I a ton of work for work... creating a service mesh using consul connect as sidecars in AWS fargate with ... terraform, spent more hours than I'd like to admit on this.

**Thoughts:** 

**Link to work:**  TBD

### Day 5: January 9, 2018

**Today's Progress**: Create frontend JS framework template, Worked on python lib/class structure, and added logging informational bits in for the serverless calls. Serverless needs to output config in log format for cloudwatch logs to better pick it up.

**Thoughts:** Class structure in python has always been a little confusing initiating a few clients, and calling apis. I think todays creation of the self__init__ structure for self initiaing boto client was really beneficial.

**Link to work:**  TBD