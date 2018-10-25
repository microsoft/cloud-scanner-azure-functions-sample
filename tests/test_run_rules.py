from unittest import TestCase
from unittest.mock import patch
from cloud_scanner.services import ResourceTagger
from azure.functions import TimerRequest
from RunRules import main


class TestRunRulesFunction(TestCase):
    @patch.object(ResourceTagger, 'process_tag_rules')
    def test_run_rules(self, mock_process_tag_rules):

        main(None)
        mock_process_tag_rules.assert_called()
