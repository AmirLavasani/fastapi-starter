import socket
import os
import py_eureka_client.eureka_client as eureka_client
from loguru import logger


EUREKA_URL = os.environ.get("EUREKA_URL")


async def register_service():
    if EUREKA_URL:
        try:
            my_ip_address = socket.gethostbyname(socket.gethostname())
            await eureka_client.init_async(
                eureka_server=EUREKA_URL,
                app_name="ai-service-template",
                instance_port=8080,
                instance_ip=my_ip_address,
                instance_host=my_ip_address,
            )
        except Exception as e:
            logger.error(f"Error Occured in Registering: {e}")
    else:
        logger.warning(
            "EUREKA_URL env variable not set. Not registering to the discovery service"
        )


async def unregister_service():
    if EUREKA_URL:
        try:
            eureka_client.stop_async()
        except Exception as e:
            logger.error(f"Error Occured in Unregistering: {e}")
