import json
import logging
import boto3
from botocore.exceptions import ClientError


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))

	try:
		return {
			"statusCode": 200,
			"body": json.dumps(event),
		}
	except Exception as e:
		logger.info(f"Failed to write event to stream: {e}")
		raise e