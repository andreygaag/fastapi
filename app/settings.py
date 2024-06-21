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

    JWT_EXPIRES: int = 6000000000
    JWT_SECRET: str = 'GrandmaLivedWithTwoCheerfulGeeseOneGrayAndTheOtherWhiteTwoCheerfulGeese'
    JWT_ALGORITHM: str = 'HS256'

    WORKERS: int = 1


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)
