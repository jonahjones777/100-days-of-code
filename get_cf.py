#!/bin/sh
import boto3
import sys
import random
import time
import os 
import re
from subprocess import call
from pprint import pprint
from lib.logger import Logger
from lib.cognito import Cognito
from lib.cognitopool import CognitoPool
from lib.write_config import Config

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
        logger.info(cognito.sign_up(clientid, username))
        logger.info(cognito.confirm_sign_up(poolid, username))
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

def write_sls_txt(textfile, directory):
        try:
                config = Config(logger)
                path, invoke = config.write_sls_info(textfile, directory)
                return path, invoke
        except Exception as e:
                logger.exception(e)


                

def write_unit_test(test_params):
        pwd = os.getcwd()
        supportFiles = pwd + "/notes-backend"
        os.chdir(supportFiles)
        unit_script = open("cli-test.sh", "w+")
        os.chmod('cli-test.sh', 0o755)
        unit_script.write("#!/bin/bash \n")
        unit_script.write('npx aws-api-gateway-cli-test \\{}'.format("\n"))
        for k, v in test_params.items():
                unit_script.writelines("--{} '{}' \\".format(k, v))
                unit_script.write('\n')


# def write_sls_info(textfile, directory):
#         with open(textfile, 'r') as f:
#                 lines = f.readlines()
#                 for line in lines:
#                         if re.search(r'POST', line):
#                                 real_url = line.split(' - ')
#                                 split_1 = real_url[-1].split('/')
#                                 length = len(split_1)
#                                 path = split_1[-1]
#                                 path = path.rstrip("\n")
#                                 print ("printing api gateway url path: {}".format(path))
#                                 invoke = ['/'.join(split_1[0:(length - 1)])]
#                                 print ("printing api invoke url: {}".format(invoke[0]))
#         pwd = os.getcwd()
#         supportFiles = pwd + directory
#         os.chdir(supportFiles)
#         if os.path.exists(textfile) == True:
#                 print ('file exists passing')
#                 pass
#         else:
#                 os.system("sls info --aws-profile here > {}}".format(textfile))
#         os.chdir(pwd)



## GET API GATWAY CRAPPP ##

# Grab info about current about the serverless deployment
path, invoke = write_sls_txt('sls.txt', "/notes-backend")
             
unit_test_dict = {}
poolid, clientid = cognito_stuff(user_name)
identtity_pool_id = cognito_identity()

unit_test_dict['username'] = user_name
unit_test_dict['password'] = password
unit_test_dict['user-pool-id'] = poolid
unit_test_dict['app-client-id'] = clientid
unit_test_dict['cognito-region'] = region
unit_test_dict['identity-pool-id'] = identtity_pool_id
unit_test_dict['invoke-url'] = invoke[0]
unit_test_dict['api-gateway-region'] = region
unit_test_dict['path-template'] = ('/' + path)
unit_test_dict['method'] ="POST"
unit_test_dict['body'] = '{"content":"hello world","attachment":"hello.jpg"}'

# # Write then execute the unit tests
# write_unit_test(unit_test_dict)
# rc = call("./cli-test.sh")
