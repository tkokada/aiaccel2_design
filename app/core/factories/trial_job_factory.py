from app.core.entities.trial_job import TrialJob


class TrialJobFactory:
    @staticmethod
    def create(hyperparameter_set: dict) -> TrialJob:
        return TrialJob(hyperparameter_set=hyperparameter_set)
