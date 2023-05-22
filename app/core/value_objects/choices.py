from pydantic import BaseModel


class Choices(BaseModel):
    values: list[str]
