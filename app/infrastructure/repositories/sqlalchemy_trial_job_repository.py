from app.core.entities.trial_job import TrialJob
from app.core.repositories.trial_job_repository import TrialJobRepository
from app.infrastructure.models import TrialJobModel
from sqlalchemy.orm import Session


class SQLAlchemyTrialJobRepository(TrialJobRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, trial_job: TrialJob):
        trial_job_model = TrialJobModel(
            id=trial_job.id,
            hyperparameter_set=trial_job.hyperparameter_set,
            execution_command=trial_job.execution_command,
            status=trial_job.status,
            result=trial_job.result,
        )
        self.session.add(trial_job_model)
        self.session.commit()

    def get(self, trial_job_id: str) -> TrialJob:
        trial_job_model = (
            self.session.query(TrialJobModel)
            .filter(TrialJobModel.id == trial_job_id)
            .first()
        )
        if trial_job_model:
            return TrialJob(
                hyperparameter_set=trial_job_model.hyperparameter_set,
                execution_command=trial_job_model.execution_command,
                status=trial_job_model.status,
                result=trial_job_model.result,
            )
        return None

    def delete(self, trial_job_id: str):
        self.session.query(TrialJobModel).filter(
            TrialJobModel.id == trial_job_id
        ).delete()
        self.session.commit()
