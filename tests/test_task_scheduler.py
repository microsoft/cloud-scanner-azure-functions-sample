from unittest import TestCase
from unittest.mock import patch
from cloud_scanner.services import TaskScheduler
from TaskScheduler import main
from azure.functions import TimerRequest


class TestTaskSchedulerFunction(TestCase):
    @patch.object(TaskScheduler, 'execute')
    def test_task_scheduler(self, mock_execute):

        main(None)
        mock_execute.assert_called()
