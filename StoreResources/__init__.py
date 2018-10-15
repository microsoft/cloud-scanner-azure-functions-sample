from cloud_scanner.services import ResourceStorage
from azure.functions import QueueMessage
from cloud_scanner_azure import services
from cloud_scanner_generic import services

from .. import settings


async def main(msg: QueueMessage):
    """
    Process payload from queue to store in registered storage provider
    :param msg: Resource payload from queue
    """
    ResourceStorage.process_queue_message(msg)
