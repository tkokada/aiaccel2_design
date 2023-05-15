from fastapi import APIRouter, Depends, HTTPException, status

from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.user import UserInvalidException, UserNotFoundException
from aiaccel2.user.infrastructure.pymongo_user_repository import PyMongoUserRepository
from aiaccel2.user.presentation.api.v1.user.user_update_request import UserUpdateRequest
from aiaccel2.user.use_cases.update_one_user_command import UpdateOneUserCommand, UpdateOneUserCommandHandler

update_one_router = APIRouter()


async def _update_one_command_handler() -> CommandHandler:
    repository = PyMongoUserRepository()
    return UpdateOneUserCommandHandler(repository)


@update_one_router.put("/api/v1/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_user(
    user_id: str,
    user_request: UserUpdateRequest,
    handler: CommandHandler = Depends(_update_one_command_handler)
) -> None:
    try:
        command = UpdateOneUserCommand(user_id, user_request.name, user_request.email)
        handler.process(command)
    except UserInvalidException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The request id: {user_id}, name: {user_request.name}, email: {user_request.email} is not valid"
        ) from exception
    except UserNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found") from exception
