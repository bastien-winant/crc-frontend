import json
import logging
import random
from datetime import datetime, timedelta

import backoff
import boto3

class Config:
	def __init__(self):
		self.delivery_stream_name = "cloud-resume-visitor-log-stream"
		self.region = "eu-central-1"


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FirehoseClient:
	"""
	AWS Firehose client to send records and monitor metrics.

	Attributes:
		config (object): Configuration object with delivery stream name and region.
		delivery_stream_name (str): Name of the Firehose delivery stream.
		region (str): AWS region for Firehose and CloudWatch clients.
		firehose (boto3.client): Boto3 Firehose client.
	"""

	def __init__(self, config):
			"""
			Initialize the FirehoseClient.

			Args:
				config (object): Configuration object with delivery stream name and region.
			"""
			self.config = config
			self.delivery_stream_name = config.delivery_stream_name
			self.region = config.region
			self.firehose = boto3.client("firehose", region_name=self.region)

	@backoff.on_exception(backoff.expo, Exception, max_tries=5, jitter=backoff.full_jitter)
	def put_record(self, record: dict):
		"""
		Put individual records to Firehose with backoff and retry.

		Args:
			record (dict): The data record to be sent to Firehose.

		This method attempts to send an individual record to the Firehose delivery stream.
		It retries with exponential backoff in case of exceptions.
		"""
		try:
			entry = self._create_record_entry(record)
			response = self.firehose.put_record(DeliveryStreamName=self.delivery_stream_name, Record=entry)
			self._log_response(response, entry)
			return response
		except Exception:
			logger.info(f"Fail record: {record}.")
			raise


	def _create_record_entry(self, record: dict) -> dict:
		"""
		Create a record entry for Firehose.

		Args:
			record (dict): The data record to be sent.

		Returns:
			dict: The record entry formatted for Firehose.

		Raises:
			Exception: If a simulated network error occurs.
		"""
		return {"Data": json.dumps(record)}

	def _log_response(self, response: dict, entry: dict):
		"""
		Log the response from Firehose.

		Args:
			response (dict): The response from the Firehose put_record API call.
			entry (dict): The record entry that was sent.
		"""
		if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
			logger.info(f"Sent record: {entry}")
		else:
			logger.info(f"Fail record: {entry}")

	def _log_batch_response(self, response: dict, batch_size: int):
		"""
		Log the batch response from Firehose.

		Args:
			response (dict): The response from the Firehose put_record_batch API call.
			batch_size (int): The number of records in the batch.
		"""
		if response.get("FailedPutCount", 0) > 0:
			logger.info(
					f'Failed to send {response["FailedPutCount"]} records in batch of {batch_size}'
			)
		else:
			logger.info(f"Successfully sent batch of {batch_size} records")


def lambda_handler(event, context):
	config = Config()
	client = FirehoseClient(config)

	try:
		response = client.put_record(event)

		return {
			"statusCode": 200,
			"body": json.dumps(response),
		}
	except Exception as e:
		logger.info(f"Put record failed after retries and backoff: {e}")