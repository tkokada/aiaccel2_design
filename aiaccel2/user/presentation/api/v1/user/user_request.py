from dataclasses import dataclass


@dataclass
class UserRequest:
    user_id: str
    name: str
    email: str
