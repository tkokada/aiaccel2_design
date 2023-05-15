from fastapi import APIRouter, Depends

from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.infrastructure.pymongo_user_repository import PyMongoUserRepository
from aiaccel2.user.presentation.api.v1.user.user_list_response import UserListResponse
from aiaccel2.user.use_cases.find_all_users_command import FindAllUsersCommand, FindAllUsersCommandHandler

find_all_router = APIRouter()


async def _find_all_command_handler() -> CommandHandler:
    repository = PyMongoUserRepository()
    return FindAllUsersCommandHandler(repository)


@find_all_router.get("/api/v1/user", response_model=UserListResponse)
def find_all_users(handler: FindAllUsersCommandHandler = Depends(_find_all_command_handler)) -> UserListResponse:
    command = FindAllUsersCommand()
    users_response = handler.process(command)
    return UserListResponse(users_response.users)
