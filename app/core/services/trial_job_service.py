from app.core.entities.trial_job import TrialJob
from app.core.repositories.trial_job_repository import TrialJobRepository


class TrialJobService:
    def __init__(self, trial_job_repository: TrialJobRepository):
        self.trial_job_repository = trial_job_repository

    def create_trial_job(self, hyperparameter_set: dict) -> TrialJob:
        trial_job = TrialJob(hyperparameter_set=hyperparameter_set)
        self.trial_job_repository.save(trial_job)
        return trial_job

    def get_trial_job(self, trial_job_id: str) -> TrialJob:
        return self.trial_job_repository.get(trial_job_id)

    def update_trial_job(self, trial_job: TrialJob) -> TrialJob:
        self.trial_job_repository.save(trial_job)
        return trial_job

    def delete_trial_job(self, trial_job_id: str):
        self.trial_job_repository.delete(trial_job_id)
