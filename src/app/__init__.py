"""
Main module for the service application.

This module contains the main entry point for running the service. It prints the version
and then starts the service by calling the run_service function.
"""


from app.version import __version__
from app.main import run_service
from loguru import logger


def main():
    """
    The main entry point for running the service.

    This function prints the version and then starts the service by calling run_service.
    """
    logger.info(f"Current version: {__version__}")
    run_service()
