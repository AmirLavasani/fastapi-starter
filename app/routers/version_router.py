from fastapi import APIRouter, status

from app.schemas.version import Version
from app.version import VERSION


router = APIRouter()


@router.get("/", response_model=Version, status_code=status.HTTP_200_OK)
async def get_app_version():
    """
    Retrieve the application version.

    Returns:
        Version: The pydantic model for app version.
    """
    return Version(version=VERSION)
