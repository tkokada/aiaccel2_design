import uuid

from aiaccel2.user.domain.command import Command
from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.command_response import CommandResponse
from aiaccel2.user.domain.user import User, UserNotFoundException
from aiaccel2.user.domain.user_repository import UserRepository


class FindOneUserCommand(Command):

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        super().__init__(uuid.uuid1())


class FindOneUserCommandResponse(CommandResponse):

    def __init__(self, user: User) -> None:
        self.user = user


class FindOneUserCommandHandler(CommandHandler):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def process(
            self,
            command: FindOneUserCommand) -> FindOneUserCommandResponse:
        user = self.repository.find(command.user_id)
        if not user:
            raise UserNotFoundException()
        return FindOneUserCommandResponse(user)
