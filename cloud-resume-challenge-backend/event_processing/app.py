import base64
import json
import boto3
from datetime import datetime

# default encoding of bytes in the posted record
ENCODING = 'utf-8'

print('Loading function')

def lambda_handler(event, context):
	output = []

	print("Received batch of {} records".format(len(event['records'])))

	for record in event['records']:
		payload = base64.b64decode(record['data']).decode(ENCODING)
		event = json.loads(payload)

		# TODO: apply transforms
		trans_event = dict(event)
		print("TRANSPORTED EVENT: ", trans_event)

		trans_payload = json.dumps(trans_event) + "\n"

		output_record = {
			'recordId': record['recordId'],
			'result': 'Ok',
			'data': base64.b64encode(trans_payload.encode(ENCODING)).decode(ENCODING)
		}
		output.append(output_record)

	return {'records': output}