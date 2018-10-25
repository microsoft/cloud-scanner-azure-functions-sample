from unittest import TestCase
from unittest.mock import patch
from cloud_scanner.services import ResourceStorage
from azure.functions import TimerRequest
from StoreResources import main
from . import FakeQueueMessage


class TestStoreResourcesFunction(TestCase):
    @patch.object(ResourceStorage, 'process_queue_message')
    def test_store_resources(self, mock_process_queue_message):

        msg = FakeQueueMessage(bytes('{}', 'utf-8'))
        main(msg)
        mock_process_queue_message.assert_called()
