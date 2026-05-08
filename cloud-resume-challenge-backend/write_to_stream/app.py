import json
import logging
import boto3
from botocore.exceptions import ClientError


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KinesisStream:
	"""Encapsulates a Kinesis stream."""

	def __init__(self, kinesis_client):
		"""
		:param kinesis_client: A Boto3 Kinesis client.
		"""
		self.kinesis_client = kinesis_client
		self.name = None
		self.details = None
		self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")


	def put_record(self, data, partition_key):
		"""
		Puts data into the stream. The data is formatted as JSON before it is passed
		to the stream.

		:param data: The data to put in the stream.
		:param partition_key: The partition key to use for the data.
		:return: Metadata about the record, including its shard ID and sequence number.
		"""
		try:
			response = self.kinesis_client.put_record(
				StreamName=self.name, Data=json.dumps(data), PartitionKey=partition_key
			)
			logger.info(f"Put record in stream {self.name}.")
		except ClientError:
			logger.exception(f"Couldn't put record in stream {self.name}.")
			raise
		else:
			return response

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))

	try:
		return {
			"statusCode": 200,
			"body": json.dumps(event),
		}
	except Exception as e:
		logger.excep(f"Failed to write event to stream: {e}")
		raise e