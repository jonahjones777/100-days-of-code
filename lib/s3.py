#!/bin/sh
import boto3
import sys
import random
import time
import os 
from pprint import pprint

class S3(object):
    def __init__(self, logger, **kwargs):
        self.logger = logger
        session = boto3.Session(profile_name='here', region_name='us-east-1')
        if kwargs is not None:
            if kwargs.get('credentials') is None:
                logger.debug("Setting up cognito BOTO3 Client with default credentials")
                self.cognito_client = session.client('s3')
            else:
                logger.debug("Setting up cognito BOTO3 Client with ASSUMED ROLE credentials")
                cred = kwargs.get('credentials')
                self.cognito_client = session.client('s3',
                                                aws_access_key_id=cred.get('AccessKeyId'),
                                                aws_secret_access_key=cred.get('SecretAccessKey'),
                                                aws_session_token=cred.get('SessionToken')
                                                )
        else:
            logger.info("There were no keyworded variables passed.")
            self.cognito_client = session.client('s3')

    def list_buckets(self):
        try:
            pool_list = self.cognito_client.list_identity_pools(
                MaxResults=30
            )
            for stuff in  (pool_list['IdentityPools']):
                if (stuff['IdentityPoolName']) == 'NotesIdentity':
                    poolid = stuff['IdentityPoolId']
                    return poolid
                    break
        except Exception as e:
            self.logger.exception(e)
            raise