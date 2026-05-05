import json
import urllib.parse
import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

s3 = boto3.client('s3')

def read_s3_object(bucket, key):
	# Get the object from the event and return its content
	try:
		response = s3.get_object(Bucket=bucket, Key=key)
		print("CONTENT TYPE: " + response['ContentType'])

		body = response['Body'].read().decode('utf-8')
		print("BODY: " + body)

		return body
	except Exception as e:
		logger.info(f'''
			Error getting object {key} from bucket {bucket}. Make sure they exist and your bucket is in the same region as this function.''')
		raise e


def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))

	bucket = event['Records'][0]['s3']['bucket']['name']
	key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

	try:
		entry = read_s3_object(bucket, key)
	except Exception as e:
		raise e


