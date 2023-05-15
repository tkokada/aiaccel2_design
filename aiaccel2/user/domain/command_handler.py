from abc import ABC, abstractmethod

from aiaccel2.user.domain.command import Command
from aiaccel2.user.domain.command_response import CommandResponse


class CommandHandler(ABC):

    @abstractmethod
    def process(self, command: Command) -> CommandResponse:
        pass
