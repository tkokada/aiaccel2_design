from fastapi import APIRouter, Depends, HTTPException, status

from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.user import User, UserNotFoundException
from aiaccel2.user.infrastructure.pymongo_user_repository import PyMongoUserRepository
from aiaccel2.user.presentation.api.v1.user.user_response import UserResponse
from aiaccel2.user.use_cases.find_one_user_command import FindOneUserCommand, FindOneUserCommandHandler

find_one_router = APIRouter()


async def _find_one_command_handler() -> CommandHandler:
    repository = PyMongoUserRepository()
    return FindOneUserCommandHandler(repository)


@find_one_router.get("/api/v1/user/{user_id}", response_model=UserResponse)
def find_user(
    user_id: str,
    handler: FindOneUserCommandHandler = Depends(_find_one_command_handler)
) -> User:
    try:
        command = FindOneUserCommand(user_id)
        user_response = handler.process(command)
    except UserNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found") from exception
    return user_response.user
