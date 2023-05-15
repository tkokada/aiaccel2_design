from fastapi import APIRouter, Depends, HTTPException, Response, status

from aiaccel2.user.domain.command_handler import CommandHandler
from aiaccel2.user.domain.user import User, UserInvalidException
from aiaccel2.user.infrastructure.pymongo_user_repository import PyMongoUserRepository
from aiaccel2.user.presentation.api.v1.user.user_request import UserRequest
from aiaccel2.user.use_cases.create_one_user_command import CreateOneUserCommand, CreateOneUserCommandHandler

create_one_router = APIRouter()


async def _create_one_command_handler() -> CommandHandler:
    repository = PyMongoUserRepository()
    return CreateOneUserCommandHandler(repository)


@create_one_router.post("/api/v1/user", response_model=User)
def create_user(
    user_request: UserRequest,
    response: Response,
    handler: CommandHandler = Depends(_create_one_command_handler)
) -> User:
    try:
        command = CreateOneUserCommand(user_request.user_id, user_request.name, user_request.email)
        handler.process(command)
        response.status_code = status.HTTP_201_CREATED
        return User(user_request.user_id, user_request.name, user_request.email)
    except UserInvalidException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The request id: {user_request.user_id}, name: {user_request.name}, email: {user_request.email} is not valid"
        ) from exception
