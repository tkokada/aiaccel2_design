from dataclasses import dataclass

from bson.errors import InvalidId
from bson.objectid import ObjectId


@dataclass
class User:
    user_id: str
    name: str
    email: str

    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email


class UserFactory:

    @staticmethod
    def make(user_id: str, name: str, email: str) -> User:
        try:
            ObjectId(user_id)
        except InvalidId as exception:
            raise UserInvalidException() from exception

        if name == "":
            raise UserInvalidException()
        if email == "":
            raise UserInvalidException()

        return User(user_id, name, email)


class UserNotFoundException(Exception):
    pass


class UserInvalidException(Exception):
    pass
