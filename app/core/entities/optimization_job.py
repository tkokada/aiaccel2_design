from datetime import datetime

# from app.core.entities.hyperparameter_definition import HyperparameterDefinition
from app.core.entities.optimization_settings import OptimizationSettings

# from app.core.entities.trial_job import TrialJob
# from app.core.value_objects.execution_command import ExecutionCommand
# from app.core.value_objects.execution_infrastructure_type import (
#    ExecutionInfrastructureType,
# )
# from app.core.value_objects.id import ID
from app.core.value_objects.name import Name
from app.utilities.uuid_generator import generate_uuid

# from app.core.value_objects.optimization_algorithm import OptimizationAlgorithm
from pydantic import UUID4, BaseModel, Field


class OptimizationJob(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
    name: Name
    optimization_settings: OptimizationSettings
    # hyperparameter_definitions: list[HyperparameterDefinition]
    # execution_infrastructure_type: ExecutionInfrastructureType
    # optimization_algorithm: OptimizationAlgorithm
    # trial_jobs: list[TrialJob]
    # execution_command: ExecutionCommand
    creation_date: datetime = datetime.now
    updated_date: datetime = datetime.now

    class Config:
        orm_mode = True


def current_datetime():
    return datetime.now()


def create_optimization_job(name, optimization_settings):
    return OptimizationJob(
        name=Name(name),
        optimization_settings=optimization_settings,
        # hyperparameter_definitions=[],
        # execution_infrastructure_type=ExecutionInfrastructureType(""),
        # optimization_algorithm=OptimizationAlgorithm(""),
        # trial_jobs=[],
        # execution_command=ExecutionCommand(""),
        creation_date=current_datetime(),
        updated_date=None,
    )


def update_optimization_job_settings(job, optimization_settings):
    job.optimization_settings = optimization_settings
    job.updated_date = current_datetime()


def update_optimization_job_user_program(job, user_program):
    job.optimization_settings.user_program = user_program
    job.updated_date = current_datetime()
