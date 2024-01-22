""" Routers Module.

    This module is responsible for registering different API routes.

"""

from fastapi import FastAPI
from .version_router import router as version_router


def register_routers(app: FastAPI):
    app.include_router(version_router, prefix="/version", tags=["version"])
