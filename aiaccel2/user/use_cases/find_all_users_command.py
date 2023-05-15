import uuid
from typing import List

from aiaccel2.user.domain.command import Command
from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.command_response import CommandResponse
from aiaccel2.user.domain.user import User
from aiaccel2.user.domain.user_repository import UserRepository


class FindAllUsersCommand(Command):

    def __init__(self) -> None:
        super().__init__(uuid.uuid1())


class FindAllUsersCommandResponse(CommandResponse):

    def __init__(self, users: List[User]) -> None:
        self.users = users


class FindAllUsersCommandHandler(CommandHandler):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def process(
            self, _command: FindAllUsersCommand
    ) -> "FindAllUsersCommandResponse":
        users: List[User] = self.repository.find_all()
        return FindAllUsersCommandResponse(users)
