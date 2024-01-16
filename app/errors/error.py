from typing import List
from pydantic import BaseModel
from fastapi import HTTPException


class NotFoundErrorResponse(BaseModel):
    type: str = "service.not_found_error"
    msg: str = "The requested resource not found"
    loc: List[str] = ["general", "not_found_error"]


HTTPNotFoundErrorResponse = HTTPException(
    status_code=404, detail=NotFoundErrorResponse().model_dump()
)


class BadRequestErrorResponse(BaseModel):
    type: str = "service.bad_request"
    msg: str = "The server cannot process the request"
    loc: List[str] = ["general", "bad_request"]


HTTPBadRequestErrorResponse = HTTPException(
    status_code=400, detail=BadRequestErrorResponse().model_dump()
)


class InternalServerErrorResponse(BaseModel):
    type: str = "service.internal_server_error"
    msg: str = "The server encountered an unexpected condition"
    loc: List[str] = ["general", "internal_server_error"]


HTTPInternalServerErrorResponse = HTTPException(
    status_code=500, detail=InternalServerErrorResponse().model_dump()
)
