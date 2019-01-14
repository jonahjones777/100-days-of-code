#!/bin/sh
import boto3
import sys
import random
import time
import os 
import re
from pprint import pprint
from lib.logger import Logger
from lib.cognito import Cognito
from lib.cognitopool import CognitoPool

session = boto3.Session(profile_name='here', region_name='us-east-1')
cognito = session.client('cognito-idp')
cognito_pool = session.client('cognito-identity')

log_level = 'info'
logger = Logger(loglevel=log_level)
init_failed = False

user_name='jonah.jones@maine.edu'
password= 'Password!23'
region = 'us-east-1'

def cognito_stuff(username, ):
    try:
        cognito = Cognito(logger)

        poolid = cognito.list_user_pools()
        logger.info('The User Pool ID is {}\n'.format(poolid))
        clientid = cognito.list_user_pool_clients(poolid)
        logger.info('The App Client ID is {}\n'.format(clientid))
        # logger.info(cognito.sign_up(clientid, username))
        # logger.info(cognito.confirm_sign_up(poolid, username))
        return poolid, clientid
    except Exception as e:
        logger.exception(e)

def cognito_identity():
    try:
        cognito = CognitoPool(logger)

        identtity_pool_id = cognito.list_identity_pools()
        logger.info('The Identity Pool ID is {}\n'.format(identtity_pool_id))
        return identtity_pool_id
    except Exception as e:
        logger.exception(e)


def write_unit_test(test_params):
    cwd = os.getcwd()
    unit_script = open("cli-test.sh", "w+")
    unit_script.write("npx aws-api-gateway-cli-test \ \n")
    for k, v in test_params.items():
        unit_script.writelines("--{}='{}' \ ".format(k, v))
        unit_script.write('\n')


unit_test_dict = {}



poolid, clientid = cognito_stuff(user_name)
identtity_pool_id = cognito_identity()

## GET API GATWAY CRAPPP ##
pwd = os.getcwd()
supportFiles = pwd + "/notes-sls"
os.chdir(supportFiles)
if os.path.exists('sls.txt') == True:
        print ('file exists passing')
        pass
else:
        os.system("sls info --aws-profile here > sls.txt")

with open('sls.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
                if re.search(r'POST', line):
                        real_url = line.split(' - ')
                        split_1 = real_url[-1].split('/')
                        length = len(split_1)
                        path = split_1[-1]
                        print ("printing api gateway url path: {}".format(path))
                        invoke = ['/'.join(split_1[0:(length - 1)])]
                        print ("printing api invoke url: {}".format(invoke[0]))
os.chdir(pwd)


unit_test_dict['username'] = user_name
unit_test_dict['password'] = password
unit_test_dict['user-pool-id'] = poolid
unit_test_dict['app-client-id'] = clientid
unit_test_dict['cognito-region'] = region
unit_test_dict['identity-pool-id'] = identtity_pool_id
unit_test_dict['invoke-url'] = invoke[0]
unit_test_dict['api-gateway-region'] = region
unit_test_dict['path-template'] = ('/' + path)
unit_test_dict['body'] = {"content":"hello world","attachment":"hello.jpg"}


write_unit_test(unit_test_dict)
