import json
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))
	return event