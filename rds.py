#!/usr/bin/env python3
import os
import boto3
import pprint
import awspricing



# AWSPRICING_USE_CACHE: Whether to use a simple file-based cache. Valid values are 0|1. Defaults to 0 (false).
#
# AWSPRICING_CACHE_PATH: Prefix to write cache files. Defaults to /tmp/awspricing.
#
# AWSPRICING_CACHE_MINUTES: Number of minutes to keep cache for. Defaults to 1440 (1 day).

os.putenv('AWSPRICING_USE_CACHE', '1')
os.putenv('AWSPRICING_CACHE_PATH', './price_cache/')
os.putenv('AWSPRICING_CACHE_MINUTES', '14400')


client = boto3.client('rds')
response = client.describe_db_instances()

print("pulling rates")
rds_offer = awspricing.offer('AmazonRDS')
print("got rates")

sku = rds_offer.search_skus(
    instance_type='db.m4.large',
    location='US East (N. Virginia)',
    database_engine='MySQL',
    license_model='No license required',
    deployment_option='Multi-AZ'
) # {'QPZNR6MYN432XTPU'}

oh1 = rds_offer.ondemand_hourly(
    'db.m4.large',
    'MySQL',
    license_model='No license required',
    deployment_option='Multi-AZ',
    region='us-east-1'
) # 0.35

oh2 = rds_offer.ondemand_monthly(
    'db.t3.xlarge',
    'MySQL',
    license_model='No license required',
    deployment_option='Multi-AZ',
    region='us-east-1'
)

print("{0}, {1}".format(oh1, oh2))



# for i in response['DBInstances']:
#     pprint.pprint(i)
#     # db_name = i['DBName']
#     db_instance_name = i['DBInstanceIdentifier']
#     db_type = i['DBInstanceClass']
#     db_storage = i['AllocatedStorage']
#     db_engine = i['Engine']
#     print("{0}, {1}, {2}".format(db_instance_name,db_type,db_storage,db_engine))
#

