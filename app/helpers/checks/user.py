from uuid import UUID

from sqlalchemy import select

from app.engines.postgres_storage import PostgresEngine
from app.models.users import UserDB


async def user_exist_by_uuid(user_uuid: UUID) -> bool:
    subquery = select(UserDB.user_uuid).where(UserDB.user_uuid == user_uuid).exists()
    return await PostgresEngine().execute(select(subquery))
