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
			trans_data = {
				'request_id': data['requestContext']['requestId'],
				'request_datetime': data['requestContext']['requestTimeEpoch'],
				'ip_address': data['requestContext']['identity'].get('sourceIp'),
				'user_agent': data['headers'].get('User-Agent'),
				'referer': data['headers'].get('Referer'),
				'desktop': data['headers'].get('CloudFront-Is-Desktop-Viewer'),
				'mobile': data['headers'].get('CloudFront-Is-Mobile-Viewer'),
				'smart_tv': data['headers'].get('CloudFront-Is-SmartTV-Viewer'),
				'tablet': data['headers'].get('CloudFront-Is-Tablet-Viewer'),
				'country': data['headers'].get('CloudFront-Viewer-Country'),
			}

			record['data'] = base64.b64encode(json.dumps(trans_data).encode('utf-8')).decode('utf-8')
			output.append(record)
		except Exception as e:
			logger.exception(f"An error occurred {e}")
			raise e

	logger.info(f"Successfully processed {len(event)} records.")
	return output
