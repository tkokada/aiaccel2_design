from app.core.entities.hyperparameter import Hyperparameter
from app.core.value_objects.name import Name
from app.utilities.uuid_generator import generate_uuid
from pydantic import UUID4, BaseModel, Field


class HyperparameterSet(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
    name: Name
    hyperparameters: list[Hyperparameter]
