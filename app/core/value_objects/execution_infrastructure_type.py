from enum import Enum


class ExecutionInfrastructureType(str, Enum):
    LOCAL = "local"
    AWS = "aws"
    ABCI = "abci"
