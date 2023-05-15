import uuid

from aiaccel2.user.domain.command import Command
from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.command_response import CommandResponse
from aiaccel2.user.domain.user import UserFactory
from aiaccel2.user.domain.user_repository import UserRepository


class CreateOneUserCommand(Command):

    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        super().__init__(uuid.uuid1())


class CreateOneUserCommandResponse(CommandResponse):
    pass


class CreateOneUserCommandHandler(CommandHandler):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def process(
            self, command: CreateOneUserCommand
    ) -> CreateOneUserCommandResponse:
        user = UserFactory.make(command.user_id, command.name, command.email)
        self.repository.save(user)
        return CreateOneUserCommandResponse()
