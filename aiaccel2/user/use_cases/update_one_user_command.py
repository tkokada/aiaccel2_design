import uuid

from aiaccel2.user.domain.command import Command
from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.command_response import CommandResponse
from aiaccel2.user.domain.user import User, UserFactory, UserNotFoundException
from aiaccel2.user.domain.user_repository import UserRepository


class UpdateOneUserCommand(Command):

    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        super().__init__(uuid.uuid1())


class UpdateOneUserCommandResponse(CommandResponse):

    def __init__(self, user: User) -> None:
        self.user = user


class UpdateOneUserCommandHandler(CommandHandler):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def process(
            self, command: UpdateOneUserCommand
    ) -> UpdateOneUserCommandResponse:
        user = UserFactory.make(user_id=command.user_id, name=command.name, email=command.email)
        response = self.repository.update(user)
        if not response:
            raise UserNotFoundException()
        return UpdateOneUserCommandResponse(response)
