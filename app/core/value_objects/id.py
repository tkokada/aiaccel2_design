import uuid

from pydantic import UUID4, BaseModel, Field


class ID(BaseModel):
    value: UUID4 = Field(default_factory=uuid.uuid4)
