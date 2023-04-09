#!/usr/bin/env python

import boto3
import pprint

client = boto3.client('rds')
response = client.describe_db_instances()



for i in response['DBInstances']:
    pprint.pprint(i)
    db_name = i['DBName']
    db_instance_name = i['DBInstanceIdentifier']
    db_type = i['DBInstanceClass']
    db_storage = i['AllocatedStorage']
    db_engine = i['Engine']
    print("{0}, {1}, {2}".format(db_instance_name,db_type,db_storage,db_engine))