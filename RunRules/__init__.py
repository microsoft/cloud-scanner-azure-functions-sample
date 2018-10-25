import azure.functions
from cloud_scanner.services import ResourceTagger
from cloud_scanner_azure import services
from cloud_scanner_generic import services
from dotenv import load_dotenv
load_dotenv('../.env')


def main(timer: azure.functions.TimerRequest):
    """
    Runs rules as defined in ResourceTagger class. Currently disabled

    :param timer: Runs on timer as defined by function.json
    :return: None
    """

    ResourceTagger.process_tag_rules()
