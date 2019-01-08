#!/bin/sh
import boto3
import sys
import random
import time
import os 
from pprint import pprint



session = boto3.Session(profile_name='here', region_name='us-east-1')
cognito = session.client('cognito-idp')


def list_user_pools(client):
    try:
        pool_list = client.list_user_pools(
            MaxResults=60
        )
        for names in pool_list['UserPools']:
            if names['Name'] == 'User-Pool-notes-backend':
                poolid=names['Id']
            else:
                break
    except Exception as e:
        print (e)
    return poolid

def list_user_pool_clients(client, pool_id):
    clientid = ''
    try:
        pool_list = client.list_user_pool_clients(
            MaxResults=60,
            UserPoolId=pool_id
        )
        for names in pool_list['UserPoolClients']:
            if names['ClientId'] != '':
                clientid=names['ClientId']
            else:
                break
    except Exception as e:
        print (e)
    return clientid   

def sign_up(client, client_id, username):
    try:
        response = client.sign_up(
            ClientId=client_id,
            Username=username,
            Password='Password!23'
        )
    except Exception as e:
        print (e)
    return

def confirm_sign_up(client, pool_id, username):
    try:
        response = client.admin_confirm_sign_up(
            UserPoolId=pool_id,
            Username=username
        )
    except Exception as e:
        print (e)
    return

poolid = list_user_pools(cognito)
print ('The User Pool ID is {}\n'.format(poolid))

clientid = list_user_pool_clients(cognito, poolid)
print ('The App Client ID is {}\n'.format(clientid))

user_name='jonah.jones@maine.edu'
pprint (sign_up(cognito, clientid, user_name))
pprint (confirm_sign_up(cognito, poolid, user_name))


    


