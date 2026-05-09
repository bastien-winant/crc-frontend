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
		# 'exists' if the table exists. Otherwise, it is set by 'create_table'.
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
			logger.error(
				"Couldn't check for existence of %s. Here's why: %s: %s",
				table_name,
				err.response["Error"]["Code"],
				err.response["Error"]["Message"],
			)
			raise
		else:
			self.table = table

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

					writer.put_item(
						Item={
							'ID': data['request_id'],
							'Epoch': data['request_datetime'],
							'IpAddress': data['ip_address'],
							'UserAgent': data['user_agent'],
							'Referer': data['referer'],
							'Desktop': data['desktop'],
							'Mobile': data['mobile'],
							'SmartTV': data['smart_tv'],
							'Tablet': data['tablet'],
							'Country': data['country']
						}
					)
		except ClientError as err:
			logger.error(
				"Couldn't load data into table %s. Here's why: %s: %s",
				self.table.name,
				err.response["Error"]["Code"],
				err.response["Error"]["Message"],
			)
			raise
		else:
			logger.info(f"Successfully wrote {len(logs)} records to table {self.config.table_name}.")

	def add_log(self, title, year, plot, rating):
		"""
		Adds a log to the table.

		:param title: The title of the log.
		:param year: The release year of the log.
		:param plot: The plot summary of the log.
		:param rating: The quality rating of the log.
		"""
		try:
			self.table.put_item(
				Item={
					"year": year,
					"title": title,
					"info": {"plot": plot, "rating": Decimal(str(rating))},
				}
			)
		except ClientError as err:
			logger.error(
				"Couldn't add log %s to table %s. Here's why: %s: %s",
				title,
				self.table.name,
				err.response["Error"]["Code"],
				err.response["Error"]["Message"],
			)
			raise

	def update_log(self, title, year, rating, plot):
		"""
		Updates rating and plot data for a log in the table.

		:param title: The title of the log to update.
		:param year: The release year of the log to update.
		:param rating: The updated rating to the give the log.
		:param plot: The updated plot summary to give the log.
		:return: The fields that were updated, with their new values.
		"""
		try:
			response = self.table.update_item(
				Key={
					"ID": data['request_id'],
					"Epoch": data['request_datetime']
				},
				UpdateExpression='''
					set
						info.ip_address=:i,
						info.user_agent=:u,
						info.referer=:r,
						info.desktop=:d,
						info.mobile=:m,
						info.smart_tv=:s,
						info.tablet=:t,
						info.country=:c
				''',
				ExpressionAttributeValues={
					":i": data['ip_address'],
					":u": data['user_agent'],
					":r": data['referer'],
					":d": data['desktop'],
					":m": data['mobile'],
					":s": data['smart_tv'],
					":t": data['tablet'],
					":c": data['country']
				},
				ReturnValues="UPDATED_NEW",
			)
		except ClientError as err:
			logger.error(
				"Couldn't update log %s in table %s. Here's why: %s: %s",
				title,
				self.table.name,
				err.response["Error"]["Code"],
				err.response["Error"]["Message"],
			)
			raise
		else:
			return response["Attributes"]

def lambda_handler(event, context):
	# Get the service resource.
	config = Config()
	dynamodb = boto3.resource('dynamodb', region_name=config.region)

	client = DynamoDBClient(config, dynamodb)
	client.exists(config.table_name)

	client.write_batch(event)