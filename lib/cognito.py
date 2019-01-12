#!/bin/sh
import boto3
import sys
import random
import time
import os 
from pprint import pprint

class Cognito(object):
    def __init__(self, logger, **kwargs):
        self.logger = logger
        session = boto3.Session(profile_name='here', region_name='us-east-1')
        if kwargs is not None:
            if kwargs.get('credentials') is None:
                logger.debug("Setting up cognito BOTO3 Client with default credentials")
                self.cognito_client = session.client('cognito-idp')
            else:
                logger.debug("Setting up cognito BOTO3 Client with ASSUMED ROLE credentials")
                cred = kwargs.get('credentials')
                self.cognito_client = session.client('cognito-idp',
                                                aws_access_key_id=cred.get('AccessKeyId'),
                                                aws_secret_access_key=cred.get('SecretAccessKey'),
                                                aws_session_token=cred.get('SessionToken')
                                                )
        else:
            logger.info("There were no keyworded variables passed.")
            self.cognito_client = session.client('cognito-idp')


    def list_user_pools(self):
        try:
            pool_list = self.cognito_client.list_user_pools(
                MaxResults=30
            )
            for stuff in  (pool_list['UserPools']):
                if (stuff['Name']) == 'User-Pool-notes-backend':
                    print  (stuff['Name'])
                    poolid = stuff['Id']
                    return poolid
                    break
        except Exception as e:
            self.logger.exception(e)
            raise

    def list_user_pool_clients(self, pool_id):
        clientid = ''
        try:
            pool_list = self.cognito_client.list_user_pool_clients(
                MaxResults=60,
                UserPoolId=pool_id
            )
            for names in pool_list['UserPoolClients']:
                if names['ClientId'] != '':
                    clientid=names['ClientId']
                    return clientid
                else:
                    break
        except Exception as e:
            self.logger.exception(e)
            raise 

    def sign_up(self, client_id, username):
        try:
            response = self.cognito_client.sign_up(
                ClientId=client_id,
                Username=username,
                Password='Password!23'
            )
        except Exception as e:
            self.logger.exception(e)
            raise

    def confirm_sign_up(self, pool_id, username):
        try:
            response = self.cognito_client.admin_confirm_sign_up(
                UserPoolId=pool_id,
                Username=username
            )
        except Exception as e:
            self.logger.exception(e)
            raise

# log_level = 'info'
# logger = Logger(loglevel=log_level)
# init_failed = False

# pool = Cognito(logger)
# poolid = pool.list_user_pools()
# print ('The User Pool ID is {}\n'.format(poolid))

# clientid = list_user_pool_clients(cognito, poolid)
# print ('The App Client ID is {}\n'.format(clientid))

# user_name='jonah.jones@maine.edu'
# pprint (sign_up(cognito, clientid, user_name))
# pprint (confirm_sign_up(cognito, poolid, user_name))





    


