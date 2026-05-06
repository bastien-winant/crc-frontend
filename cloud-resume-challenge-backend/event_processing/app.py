import base64
import json
import boto3
from datetime import datetime

# default encoding of bytes in the posted record
ENCODING = 'utf-8'

def lambda_handler(event, context):
	output = []

	for record in event['records']:
		payload = base64.b64decode(record['data']).decode(ENCODING)
		event = json.loads(payload)

		try:
			trans_event = {
				'request_id': event['requestContext']['requestId'],
				'request_datetime': event['requestContext']['requestTimeEpoch'],
				'ip_address': event['requestContext']['identity'].get('sourceIp'),
				'user_agent': event['headers'].get('User-Agent'),
				'desktop': event['headers'].get('CloudFront-Is-Desktop-Viewer'),
				'mobile': event['headers'].get('CloudFront-Is-Mobile-Viewer'),
				'smart_tv': event['headers'].get('CloudFront-Is-SmartTV-Viewer'),
				'tablet': event['headers'].get('CloudFront-Is-Tablet-Viewer'),
				'country': event['headers'].get('CloudFront-Viewer-Country'),
			}

			trans_payload = json.dumps(trans_event) + "\n"

			output_record = {
				'recordId': record['recordId'],
				'result': 'Ok',
				'data': base64.b64encode(trans_payload.encode(ENCODING)).decode(ENCODING)
			}
			output.append(output_record)
		except Exception as e:
			logger.info(f"Failed to process event: {event}.")
			raise e

	return {'records': output}