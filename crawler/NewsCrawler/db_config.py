import boto3
import json

# for local environment
session = boto3.Session(profile_name='ybigta-conference')

client = session.client('s3')
obj = client.get_object(Bucket='naver-news-dev', Key='config/db_config.json')
CONFIG = json.loads(obj['Body'].read())
