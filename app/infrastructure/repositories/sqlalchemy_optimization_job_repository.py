import json

from app.core.entities.optimization_job import OptimizationJob
from app.core.repositories.optimization_job_repository import OptimizationJobRepository
from app.infrastructure.models import OptimizationJobModel
from sqlalchemy.orm import Session


class SQLAlchemyOptimizationJobRepository(OptimizationJobRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, optimization_job: OptimizationJob):
        optimization_settings = optimization_job.optimization_settings.dict()
        # optimization_settings["id"] = str(optimization_settings["id"])

        optimization_job_model = OptimizationJobModel(
            id=str(optimization_job.id),
            name=optimization_job.name,
            optimization_settings=json.dumps(optimization_settings),
            # optimization_settings=optimization_job.optimization_settings,
            creation_date=optimization_job.creation_date,
            updated_date=optimization_job.updated_date,
        )
        self.session.add(optimization_job_model)
        self.session.commit()

    def get(self, optimization_job_id: str) -> OptimizationJob:
        optimization_job_model = (
            self.session.query(OptimizationJobModel)
            .filter(OptimizationJobModel.id == optimization_job_id)
            .first()
        )
        if optimization_job_model:
            return OptimizationJob(
                name=optimization_job_model.name,
                optimization_settings=optimization_job_model.optimization_settings,
                creation_date=optimization_job_model.creation_date,
                updated_date=optimization_job_model.updated_date,
            )
        return None

    def delete(self, optimization_job_id: str):
        self.session.query(OptimizationJobModel).filter(
            OptimizationJobModel.id == optimization_job_id
        ).delete()
        self.session.commit()
