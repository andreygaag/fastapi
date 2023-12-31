from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class User(BaseModel):
    user_uuid: UUID | None = Field(None, examples=uuid4())
    username: str = Field(example='big_big_boss')


class UserCreate(User):
    password: str = Field(example='very secret password')
