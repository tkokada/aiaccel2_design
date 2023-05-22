from app.core.entities.hyperparameter_definition_set import \
    HyperparameterDefinitionSet
from app.core.value_objects.execution_infrastructure_type import \
    ExecutionInfrastructureType
from app.core.value_objects.optimization_algorithm import OptimizationAlgorithm
from app.utilities.uuid_generator import generate_uuid
from pydantic import UUID4, BaseModel, Field


class OptimizationSettings(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
    infrastructure_type: ExecutionInfrastructureType
    algorithm: OptimizationAlgorithm
    num_trials: int
    hyperparameter_definition_set: HyperparameterDefinitionSet
    seed: int = None
    user_program: str = None
