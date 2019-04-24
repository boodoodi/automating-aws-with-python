# coding: utf-8
import boto3
session = boto3.Session(profile_name='boodoo')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automatingboodoo-boto3')
get_ipython().run_line_magic('history', '')
new_bucket = s3.create_bucket(Bucket='automatingboodoo-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket = s3.create_bucket(Bucket='automatingboodoo-boto3', CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
new_bucket
for bucket in s3.buckets.all():
    print(bucket)
    
