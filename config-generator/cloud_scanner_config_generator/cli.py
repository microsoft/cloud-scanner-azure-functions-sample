import click
from cloud_scanner.contracts import StorageContainerFactory, CloudConfigGenerator
# Load and register required services
from cloud_scanner_azure import services
from cloud_scanner_generic import services
import os
from dotenv import load_dotenv
load_dotenv()


@click.command()
@click.option('-t', '--types', type=click.STRING, required=True,
              help="Resource types for which to scan in cloud subscriptions, separated by comma")
@click.option('-p', '--providers', type=click.STRING, required=True)
def cli(types, providers):
    resource_type_list = types.split(',')
    provider_list = providers.split(',')
    storage_conatiner = StorageContainerFactory.create()
    config_generator = CloudConfigGenerator(storage_conatiner)
    cloud_config = config_generator.generate_config(provider_list, resource_type_list)
    config_generator.output_config(cloud_config)
