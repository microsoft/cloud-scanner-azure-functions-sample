from unittest import TestCase
from unittest.mock import patch
from cloud_scanner.services import ResourceScanner
from azure.functions import TimerRequest
from ScanResources import main
from . import FakeQueueMessage


class TestScanResourcesFunction(TestCase):
    @patch.object(ResourceScanner, 'process_queue_message')
    def test_run_rules(self, mock_process_queue_message):

        msg = FakeQueueMessage(bytes('{}', 'utf-8'))
        main(msg)
        mock_process_queue_message.assert_called()
