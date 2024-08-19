from fastapi import FastAPI, Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.routers import routesUser
from fastapi.security import HTTPBearer

app = FastAPI(
    title="FastApi-Project",
    dependencies=[Depends(HTTPBearer(
        scheme_name="Bearer",
        auto_error=False,
        description="JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\"",
    ))],
    docs_url="/docs",
    openapi_url="/openapi.json",
    root_path="/fast-api-python"
)

origins = []

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

app.include_router(routesUser.router)

@app.exception_handler(RequestValidationError)
async def validationExceptionHandler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": error['loc'][-1],
            "message": error['msg'].replace("Value error, ", "")
        })
    
    return JSONResponse(
        status_code=412,
        content=errors
    )

@app.middleware('http')
async def tempoMiddleware(request: Request, next):
    print('Interceptou Chegada...')

    response = await next(request)

    print('Interceptou Volta ...')

    return response

