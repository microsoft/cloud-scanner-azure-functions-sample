import azure.functions
from cloud_scanner.services import ResourceScanner
from cloud_scanner_azure import services
from cloud_scanner_generic import services

from .. import settings


async def main(msg: azure.functions.QueueMessage):
    """
    Process task message from queue for resource scanning
    :param msg: Task from queue
    """
    ResourceScanner.process_queue_message(msg)
