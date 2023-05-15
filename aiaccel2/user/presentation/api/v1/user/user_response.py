from dataclasses import dataclass


@dataclass
class UserResponse:
    user_id: str
    name: str
    email: str
