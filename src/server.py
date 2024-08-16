from fastapi import FastAPI, Request, BackgroundTasks, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routes_user
from src.jobs.write_notification import write_notification
from fastapi.security import HTTPBearer

app = FastAPI(
    title="FastApi-Project",
    dependencies=[Depends(HTTPBearer(
        scheme_name="Bearer",
        auto_error=False,
        description="JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\"",
    ))],
)

origins = []

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

# app.include_router(routes_auth.router, prefix="/auth")

app.include_router(routes_user.router)

@app.middleware('http')
async def tempoMiddleware(request: Request, next):
    print('Interceptou Chegada...')

    response = await next(request)

    print('Interceptou Volta ...')

    return response

