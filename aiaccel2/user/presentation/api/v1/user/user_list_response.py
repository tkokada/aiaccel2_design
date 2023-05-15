from dataclasses import dataclass
from typing import List

from aiaccel2.user.domain.user import User


@dataclass
class UserListResponse:
    users: List[User]
