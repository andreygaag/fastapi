from app.repositories.user import UserRepository
from app.schemes.users import User, UserCreate
from app.services.auth import AuthService


class UserService:
    def __init__(self):
        self.user_repository: UserRepository = UserRepository()

    async def create_or_update_user(self, user_data: UserCreate) -> User:
        if user_data.password:
            user_data.password = AuthService.hash_password(user_data.password)

        user_dict = user_data.model_dump(exclude_none=True)
        user_data = await self.user_repository.create_or_update_user(user_dict)
        return User(**user_data.__dict__)
