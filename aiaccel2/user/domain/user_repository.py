from abc import ABC, abstractmethod
from typing import List, Optional

from aiaccel2.user.domain.user import User


class UserRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> str:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass
