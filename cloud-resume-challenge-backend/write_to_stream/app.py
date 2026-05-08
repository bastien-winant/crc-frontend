import json
import logging
import boto3
from botocore.exceptions import ClientError


class Config:
	def __init__(self):
		self.name = "cloud-resume-visitor-log-stream"
		self.region = "eu-central-1"


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KinesisStreamClient:
	"""
    AWS Kinesis Stream client to receive and send records.

    Attributes:
			config (object): Configuration object with delivery stream name and region.
			kinesis_stream_name (str): Name of the Firehose delivery stream.
			region (str): AWS region for Firehose and CloudWatch clients.
			kinesis_client (boto3.client): Boto3 Kinesis client.
			stream_exists_waiter (boto3.client): Boto3 Kinesis Stream client.
    """

	def __init__(self, config):
		"""
		:param config (object): Configuration object with delivery stream name and region.
		"""
		self.config = config
		self.name = config.name
		self.region = config.region
		self.kinesis_client = boto3.client('kinesis', region_name=self.region)
		self.stream_exists_waiter = self.kinesis_client.get_waiter("stream_exists")


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
				StreamName=self.name, Data=json.dumps(data), PartitionKey=data['requestContext']['requestId']
			)
			logger.info(f"Put record in stream {self.name}.")
		except ClientError:
			logger.exception(f"Couldn't put record in stream {self.name}.")
			raise
		else:
			return response

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))

	config = Config()
	client = KinesisStreamClient(config)

	try:
		response = client.put_record(data=event, partition_key=config.name)
		return {
			"statusCode": 200,
			"body": json.dumps(response),
		}
	except Exception as e:
		logger.exception(f"Failed to write event to stream: {e}")
		raise e