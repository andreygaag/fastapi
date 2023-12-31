from uuid import uuid4

from sqlalchemy import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseDB


class UserDB(BaseDB):
    __tablename__ = 'users'   # noqa
    user_uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=True)

    @hybrid_property
    def full_name(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.last_name}'
