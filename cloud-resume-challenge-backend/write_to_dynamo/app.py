import json
import logging
import boto3
import base64
from botocore.exceptions import ClientError

class Config:
	def __init__(self):
		self.table_name = "cloud-resume-visitor-logs"
		self.region = "eu-central-1"


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DynamoDBClient:
	def __init__(self, config, dyn_resource):
		"""
		:param dyn_resource: A Boto3 DynamoDB resource.
		"""
		self.config = config
		self.dyn_resource = dyn_resource
		# The table variable is set during the scenario in the call to
		# 'exists' if the table exists. Otherwise, an error is raised
		self.table = None

	def exists(self, table_name):
		"""
		Determines whether a table exists. As a side effect, stores the table in
		a member variable.

		:param table_name: The name of the table to check.
		"""
		try:
			table = self.dyn_resource.Table(table_name)
		except ClientError as err:
			logger.error(f"""
				Couldn't check for existence of {table_name}.
				Here's why: {err.response["Error"]["Code"]}: {err.response["Error"]["Message"]}
			""")
			raise
		else:
			self.table = table

	def write_item(self, writer, item_data):
		writer.put_item(
			Item={
				'ID': item_data['request_id'],
				'Epoch': item_data['request_datetime'],
				'IpAddress': item_data['ip_address'],
				'UserAgent': item_data['user_agent'],
				'Referer': item_data['referer'],
				'Desktop': item_data['desktop'],
				'Mobile': item_data['mobile'],
				'SmartTV': item_data['smart_tv'],
				'Tablet': item_data['tablet'],
				'Country': item_data['country']
			}
		)

	def write_batch(self, logs):
		"""
		Fills an Amazon DynamoDB table with the specified data, using the Boto3
		Table.batch_writer() function to put the items in the table.
		Inside the context manager, Table.batch_writer builds a list of
		requests. On exiting the context manager, Table.batch_writer starts sending
		batches of write requests to Amazon DynamoDB and automatically
		handles chunking, buffering, and retrying.

		:param logs: The data to put in the table. Each item must contain at least
									 the keys required by the schema that was specified when the
									 table was created.
		"""
		try:
			with self.table.batch_writer() as writer:
				for record in logs:
					payload = base64.b64decode(record['data']).decode('utf-8')
					data = json.loads(payload)
					self.write_item(writer, data)
		except ClientError as err:
			logger.error(f'''
				Couldn't load data into table {self.table.name}.
				Here's why: {err.response["Error"]["Code"]}: {err.response["Error"]["Message"]}
			''')
			raise
		else:
			logger.info(f"Successfully wrote {len(logs)} records to table {self.config.table_name}.")

def lambda_handler(event, context):
	# Get the service resource.
	config = Config()
	dynamodb = boto3.resource('dynamodb', region_name=config.region)

	client = DynamoDBClient(config, dynamodb)
	client.exists(config.table_name)

	client.write_batch(event)