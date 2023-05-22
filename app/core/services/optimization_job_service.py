from app.core.entities.optimization_job import OptimizationJob
from app.core.repositories.hyperparameter_definition_repository import (
    HyperparameterDefinitionRepository,
)
from app.core.repositories.optimization_job_repository import OptimizationJobRepository
from app.core.repositories.optimization_settings_repository import (
    OptimizationSettingsRepository,
)
from app.core.repositories.trial_job_repository import TrialJobRepository


class OptimizationJobService:
    def __init__(
        self,
        optimization_job_repository: OptimizationJobRepository,
        hyperparameter_definition_repository: HyperparameterDefinitionRepository,
        optimization_settings_repository: OptimizationSettingsRepository,
        trial_job_repository: TrialJobRepository,
    ):
        self.optimization_job_repository = optimization_job_repository
        self.hyperparameter_definition_repository = hyperparameter_definition_repository
        self.optimization_settings_repository = optimization_settings_repository
        self.trial_job_repository = trial_job_repository

    def create_optimization_job(
        self, optimization_job: OptimizationJob
    ) -> OptimizationJob:
        self.optimization_job_repository.save(optimization_job)
        return optimization_job

    def get_optimization_job(self, optimization_job_id: str) -> OptimizationJob:
        return self.optimization_job_repository.get(optimization_job_id)

    def get_optimization_jobs(self) -> list[OptimizationJob]:
        return self.optimization_job_repository.get_all()

    def update_optimization_job(
        self, optimization_job: OptimizationJob
    ) -> OptimizationJob:
        self.optimization_job_repository.save(optimization_job)
        return optimization_job

    def delete_optimization_job(self, optimization_job_id: str):
        self.optimization_job_repository.delete(optimization_job_id)
