from fastapi import FastAPI, Depends, exception_handlers
from starlette import status
from starlette.responses import JSONResponse

from api import api_router


async def not_found(request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": [{"msg": "Not Found."}]}
    )

exception_handlers = {404: not_found}

app = FastAPI(exception_handlers=exception_handlers, openapi_url="")

api = FastAPI(
    title="Research project API",
    description="Welcome to Image Similarity API documentation! Here you will able to discover all of the ways you can interact with the Image Similarity API.",
    root_path="/api/v1",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
    redoc_url="/redoc",
)

api.include_router(api_router)

app.mount("/api/v1", app=api)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="210.115.229.254", port=8000)