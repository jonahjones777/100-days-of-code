#!/bin/python
import sys
import random
import time
import os 
import re
from subprocess import call
from pprint import pprint
from botocore.exceptions import ClientError


class Config(object):
    def __init__(self, logger):
        self.logger = logger

    def write_sls_info(self, textfile, directory):
        try:
            pwd = os.getcwd()
            supportFiles = pwd + directory
            os.chdir(supportFiles)
            if os.path.exists(textfile) == True:
                    print ('file exists passing')
                    pass
            else:
                    os.system("sls info --aws-profile here > {}".format(textfile))
            with open(textfile, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                            if re.search(r'POST', line):
                                    real_url = line.split(' - ')
                                    split_1 = real_url[-1].split('/')
                                    length = len(split_1)
                                    path = split_1[-1]
                                    path = path.rstrip("\n")
                                    print ("printing api gateway url path: {}".format(path))
                                    invoke = ['/'.join(split_1[0:(length - 1)])]
                                    print ("printing api invoke url: {}".format(invoke[0]))
            os.chdir(pwd)
            return path, invoke
        except Exception as e:
            print (e)



