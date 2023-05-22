from pydantic import BaseModel


class ExecutionCommand(BaseModel):
    value: str
