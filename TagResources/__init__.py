from cloud_scanner.services import ResourceTagger
from azure.functions import QueueMessage
from cloud_scanner_azure import services
from cloud_scanner_generic import services
from dotenv import load_dotenv
load_dotenv('../.env')


def main(msg: QueueMessage):
    """
    Process resource payload from queue for tagging
    :param msg: Resource payload from queue
    """

    ResourceTagger.process_queue_message(msg)
