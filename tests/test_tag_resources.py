from unittest import TestCase
from unittest.mock import patch
from cloud_scanner.services import ResourceTagger
from azure.functions import TimerRequest
from TagResources import main
from . import FakeQueueMessage


class TestTagResourcesFunction(TestCase):
    @patch.object(ResourceTagger, 'process_queue_message')
    def test_tag_resources(self, mock_process_queue_message):

        msg = FakeQueueMessage(bytes('{}', 'utf-8'))
        main(msg)
        mock_process_queue_message.assert_called()
