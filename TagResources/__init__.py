import sys
import os
sys.path.append(os.path.abspath(""))

import settings
from azure.functions import QueueMessage
from cloud_scanner.services import ResourceTagger
from cloud_scanner_azure import services
from cloud_scanner_generic import services


def main(msg: QueueMessage):
    """
    Process resource payload from queue for tagging
    :param msg: Resource payload from queue
    """
    ResourceTagger.process_queue_message(msg)
