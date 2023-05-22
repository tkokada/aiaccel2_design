from app.core.entities.trial_job import TrialJob


class TrialJobRepository:
    def __init__(self):
        self.trial_jobs: list[TrialJob] = []

    def create(self, trial_job: TrialJob) -> TrialJob:
        self.trial_jobs.append(trial_job)
        return trial_job

    def get_all(self) -> list[TrialJob]:
        return self.trial_jobs

    def get_by_id(self, job_id: str) -> TrialJob:
        for job in self.trial_jobs:
            if job.id == job_id:
                return job
        return None

    def update(self, trial_job: TrialJob) -> TrialJob:
        for i, job in enumerate(self.trial_jobs):
            if job.id == trial_job.id:
                self.trial_jobs[i] = trial_job
                return trial_job
        return None

    def delete(self, job_id: str) -> bool:
        for i, job in enumerate(self.trial_jobs):
            if job.id == job_id:
                del self.trial_jobs[i]
                return True
        return False
