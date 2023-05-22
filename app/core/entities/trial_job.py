from app.core.value_objects.hyperparameter_values import HyperparameterValues
from app.core.value_objects.trial_job_result import TrialJobResult
from app.core.value_objects.trial_job_status import TrialJobStatus
from app.utilities.uuid_generator import generate_uuid
from pydantic import UUID4, BaseModel, Field


class TrialJob(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
    hyperparameter_values: HyperparameterValues
    execution_command: str = None
    status: TrialJobStatus = None
    result: TrialJobResult = None
