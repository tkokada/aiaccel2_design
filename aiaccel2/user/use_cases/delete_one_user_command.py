import uuid

from aiaccel2.user.domain.command import Command
from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.command_response import CommandResponse
from aiaccel2.user.domain.user_repository import UserRepository


class DeleteOneUserCommand(Command):

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        super().__init__(uuid.uuid1())


class DeleteOneUserCommandResponse(CommandResponse):
    pass


class DeleteOneUserCommandHandler(CommandHandler):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def process(
            self, command: DeleteOneUserCommand
    ) -> DeleteOneUserCommandResponse:
        self.repository.delete(command.user_id)
        return DeleteOneUserCommandResponse()
