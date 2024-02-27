"""
    Main script of AI Service Template.

    This script setups the API server using FastAPI.

"""

import os
from fastapi import FastAPI
from app.routers import register_routers
from contextlib import asynccontextmanager
from loguru import logger
import gradio as gr

from app.version import __version__
from app.interface import get_gr_interface
from app.utils.eureka import register_service, unregister_service


service_description = """
# AI Service Template 🚀
Welcome to the AI Service Template repository! 🤖 This template is designed for building AI services
using FastAPI as the REST API server, with Docker and docker-compose for containerization. 🐳

### GET `/version`

This endpoints return the version of the code.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("starting up the app...".upper())
    await register_service()

    yield

    logger.debug("shutting down gracefully...".upper())
    await unregister_service()


app = FastAPI(
    lifespan=lifespan,
    title="FastAPI AI Service Template",
    description=service_description,
    summary="This template is designed for building AI services using FastAPI as the REST API server",
    version=__version__,
    # root_path=os.environ.get("FASTAPI_ROOT_PATH", "/api/v1"),
    docs_url=os.environ.get(
        "FASTAPI_DOCS_URL", "/docs"
    ),
    openapi_url=os.environ.get(
        "FASTAPI_OPENAPI_URL", "/openapi.json"
    ),
)

if os.environ.get("DEV_MODE", "off") == "on":
    logger.debug("dev mode on. adding gradio interface...".upper())
    app = gr.mount_gradio_app(
        app,
        get_gr_interface(),
        path=os.environ.get(
            "FASTAPI_GRADIO_INTERFACE_URL", "/ui"
        )
    )

register_routers(app)


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI AI Service Template"}


def run_service(host: str = "0.0.0.0", port: int = 8080):
    import uvicorn

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_service()
