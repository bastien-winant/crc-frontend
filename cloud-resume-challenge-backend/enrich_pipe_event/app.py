import json
import logging
import base64


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
	output = []

	for record in event:
		try:
			# decode the payload data
			payload = base64.b64decode(record['data']).decode('utf-8')
			data = json.loads(payload)

			# Do custom processing on the payload here

			record['data'] = base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')
			output.append(record)
		except Exception as e:
			logger.exception(f"An error occurred {e}")
			raise e

	logger.info(f"Successfully processed {len(event)} records.")
	return output
