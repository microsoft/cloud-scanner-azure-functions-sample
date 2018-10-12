import pdb
from setuptools import setup, find_packages
setup(
    name="cloud_scanner_config_generator",
    version='0.1',
    description="Cloud Scanner - Config Generator",
    url="",
    author="Tanner Barlow",
    author_email="tanner.barlow12@gmail.com",
    license="MIT",
    packages=['cloud_scanner_config_generator'],
    entry_points={
        'console_scripts': [
            'generate-config = cloud_scanner_config_generator.cli:cli'
        ]
    },
    install_requires=["click"]
)