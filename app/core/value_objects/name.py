from pydantic import BaseModel


class Name(BaseModel):
    value: str
