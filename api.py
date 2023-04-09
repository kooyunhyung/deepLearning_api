from typing import Optional, List

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from shirts.views import router as shirts_router
from coat.views import router as coat_router
from hood_t.views import router as hood_t_router
from sweater.views import router as sweater_router
from jumper.views import router as jumper_router
from dress.views import router as dress_router

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
api_router.include_router(coat_router, tags=["coat"])
api_router.include_router(hood_t_router, tags=["hood_t"])
api_router.include_router(sweater_router, tags=["sweater"])
api_router.include_router(jumper_router, tags=["jumper"])
api_router.include_router(dress_router, tags=["dress"])