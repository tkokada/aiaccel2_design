from fastapi import APIRouter, Depends, status

from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.infrastructure.pymongo_user_repository import PyMongoUserRepository
from aiaccel2.user.use_cases.delete_one_user_command import DeleteOneUserCommand, DeleteOneUserCommandHandler

delete_one_router = APIRouter()


async def _delete_one_command_handler() -> CommandHandler:
    repository = PyMongoUserRepository()
    return DeleteOneUserCommandHandler(repository)


@delete_one_router.delete("/api/v1/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: str,
    handler: CommandHandler = Depends(_delete_one_command_handler)
) -> None:
    command = DeleteOneUserCommand(user_id)
    handler.process(command)
