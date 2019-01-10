#!/bin/sh
import boto3
import sys
import random
import time
import os 
from pprint import pprint
from lib.logger import Logger
from lib.cognito import Cognito

session = boto3.Session(profile_name='here', region_name='us-east-1')
cognito = session.client('cognito-idp')

log_level = 'info'
logger = Logger(loglevel=log_level)
init_failed = False

def cognito_stuff(username, ):
    try:
        cognito = Cognito(logger)

        poolid = cognito.list_user_pools()
        logger.info('The User Pool ID is {}\n'.format(poolid))
        clientid = cognito.list_user_pool_clients(poolid)
        logger.info('The App Client ID is {}\n'.format(clientid))
        logger.info(cognito.sign_up(clientid, username))
        logger.info(cognito.confirm_sign_up(poolid, username))
    except Exception as e:
        logger.exception(e)

        
user_name='jonah.jones@maine.edu'
cognito_stuff(user_name)