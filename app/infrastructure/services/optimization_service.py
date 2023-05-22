from app.core.entities.optimization_job import OptimizationJob
from app.core.entities.trial_job import TrialJob
from app.core.repositories.optimization_job_repository import OptimizationJobRepository
from app.core.repositories.trial_job_repository import TrialJobRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SQLAlchemyOptimizationService:
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.optimization_job_repository = OptimizationJobRepository(self.session)
        self.trial_job_repository = TrialJobRepository(self.session)

    def create_optimization_job(self, optimization_job: OptimizationJob):
        self.optimization_job_repository.create(optimization_job)

    def get_optimization_job(self, optimization_job_id: str) -> OptimizationJob:
        return self.optimization_job_repository.get(optimization_job_id)

    def delete_optimization_job(self, optimization_job_id: str):
        self.optimization_job_repository.delete(optimization_job_id)

    def create_trial_job(self, trial_job: TrialJob):
        self.trial_job_repository.create(trial_job)

    def get_trial_job(self, trial_job_id: str) -> TrialJob:
        return self.trial_job_repository.get(trial_job_id)

    def delete_trial_job(self, trial_job_id: str):
        self.trial_job_repository.delete(trial_job_id)
