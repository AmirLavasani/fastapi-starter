from typing import List
from pydantic import BaseModel
from fastapi import HTTPException


class GeneralNotFoundErrorResponse(BaseModel):
    type: str = "service.not_found_error"
    msg: str = "The requested resource not found"
    loc: List[str] = ["general", "not_found_error"]


HTTPGeneralNotFoundResponse = HTTPException(
    status_code=404, detail=GeneralNotFoundErrorResponse().model_dump()
)


class GeneralInternalServerErrorResponse(BaseModel):
    type: str = "service.internal_server_error"
    msg: str = "The server encountered an unexpected condition"
    loc: List[str] = ["general", "internal_server_error"]


HTTPGeneralInternalServerErrorResponse = HTTPException(
    status_code=500, detail=GeneralInternalServerErrorResponse().model_dump()
)
