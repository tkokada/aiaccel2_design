from collections import defaultdict
from typing import Dict, List, Optional

from aiaccel2.user.domain.user import User
from aiaccel2.user.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self) -> None:
        self.users: Dict[str, User] = defaultdict()

    def find_all(self) -> List[User]:
        return list(self.users.values())

    def find(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def save(self, user: User) -> None:
        self.users[user.user_id] = user

    def delete(self, user_id: str) -> None:
        del self.users[user_id]

    def update(self, user: User) -> Optional[User]:
        self.users[user.user_id] = user
        return user
