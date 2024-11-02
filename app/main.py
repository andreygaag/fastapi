from contextlib import asynccontextmanager
from random import random

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app.engines.postgres_storage import PostgresEngine
from app.routers import router
from app.schemes.users import UserCreate
from app.services.users import UserService
from app.settings import settings


async def init_postgres() -> None:
    db: PostgresEngine = PostgresEngine()
    await db.create_tables()


async def init_user() -> None:
    user_service: UserService = UserService()
    await user_service.create_or_update_user(
        UserCreate(user_uuid='00000000-0000-4000-0000-000000000001', username='admin', password='admin')
    )


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await init_postgres()
    await init_user()
    yield


app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    docs_url=settings.DOC_URL,
    openapi_url=settings.OPENAPI_URL,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.SERVER_HOST,
        port=int(settings.SERVER_PORT),
        log_level=settings.LOG_LEVEL,
    )
