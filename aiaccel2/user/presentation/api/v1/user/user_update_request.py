from dataclasses import dataclass


@dataclass
class UserUpdateRequest:
    name: str
    email: str
