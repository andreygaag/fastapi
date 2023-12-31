from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEVELOP: bool = False
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8989
    TITLE: str = 'API'
    VERSION: str = 'v1.0'
    DOC_URL: str = '/docs'
    OPENAPI_URL: str = '/openapi.json'
    LOG_LEVEL: str = 'debug'
    POSTGRES_URI: str = (
        'postgresql+asyncpg://project_name_user:project_name_password@project_name_postgres:5432/project_name_postgres'
    )
    POSTGRES_POOL_SIZE: int = 20
    POSTGRES_MAX_OVERFLOW: int = 5

    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379
    REDIS_USER: str = 'project_name_user'
    REDIS_PASSWORD: str = 'project_name_password'
    REDIS_DB_NUM: int = 0

    JWT_EXPIRES: int = 60
    JWT_SECRET: str = 'some_jwt_secret'
    JWT_ALGORITHM: str = 'HS256'
    SEARCH_LIMIT_SIZE: int = 25
    WORKERS: int = 1

    PAGINATION_PAGE: int = 1
    PAGINATION_PAGE_SIZE: int = 25


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)
