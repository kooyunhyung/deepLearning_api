from typing import Optional, List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from shirts.views import router as shirts_router
from shoes.views import router as shoes_router
from student.views import router as student_router

class ErrorMessage(BaseModel):
    msg: str

class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]

api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)

api_router.include_router(shirts_router, tags=["shirts"])
api_router.include_router(shoes_router, tags=["shoes"])
api_router.include_router(student_router, tags=["students"])