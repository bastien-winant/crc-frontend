import json
import logging
import boto3
import base64

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))

	for record in event['Records']:
		try:
			print(f"Processed Kinesis Event - EventID: {record['eventID']}")
			record_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
			print(f"Record Data: {record_data}")
		# TODO: Do interesting work based on the new data
		except Exception as e:
			print(f"An error occurred {e}")
			raise e
	print(f"Successfully processed {len(event['Records'])} records.")