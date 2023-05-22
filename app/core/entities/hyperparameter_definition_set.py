from app.core.entities.hyperparameter_definition import HyperparameterDefinition
from app.utilities.uuid_generator import generate_uuid
from pydantic import UUID4, BaseModel, Field


class HyperparameterDefinitionSet(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
    hyperparameter_definitions: list[HyperparameterDefinition]
