import azure.functions
from .. import settings
from cloud_scanner.services import TaskScheduler
from cloud_scanner_azure import services
from cloud_scanner_generic import services


def main(timer: azure.functions.TimerRequest):
    """
    Schedule tasks for resource scanning on timed request
    :param timer: Timer defined by `function.json`
    """

    TaskScheduler.execute()
