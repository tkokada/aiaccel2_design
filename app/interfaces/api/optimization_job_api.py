from app.core.entities.optimization_job import OptimizationJob
from app.core.repositories.hyperparameter_definition_repository import (
    HyperparameterDefinitionRepository,
)
from app.core.repositories.optimization_settings_repository import (
    OptimizationSettingsRepository,
)
from app.core.repositories.trial_job_repository import TrialJobRepository
from app.core.services.optimization_job_service import OptimizationJobService
from app.infrastructure.databases.database import get_session

# from app.core.repositories.optimization_job_repository import OptimizationJobRepository
from app.infrastructure.repositories.sqlalchemy_optimization_job_repository import (
    SQLAlchemyOptimizationJobRepository,
)
from fastapi import APIRouter

router = APIRouter()
session = get_session()
optimization_job_repository = SQLAlchemyOptimizationJobRepository(session=session)
hyperparameter_definition_repository = HyperparameterDefinitionRepository()
optimization_settings_repository = OptimizationSettingsRepository()
trial_job_repository = TrialJobRepository()
optimization_job_service = OptimizationJobService(
    optimization_job_repository,
    hyperparameter_definition_repository,
    optimization_settings_repository,
    trial_job_repository,
)


@router.post("/optimization_jobs")
def create_optimization_job(job: OptimizationJob):
    try:
        optimization_job_service.create_optimization_job(job)
        return {"message": "Optimization job created successfully"}
    except Exception as e:
        return {"message": "Error creating optimization job", "error": str(e)}


@router.get("/optimization_jobs/{job_id}")
def get_optimization_job(job_id: str):
    try:
        job = optimization_job_repository.get_optimization_job(job_id)
        return {"job": job}
    except Exception as e:
        return {"message": "Error retrieving optimization job", "error": str(e)}


@router.get("/optimization_jobs")
def get_all_optimization_jobs():
    try:
        jobs = optimization_job_repository.get_all_optimization_jobs()
        return {"jobs": jobs}
    except Exception as e:
        return {"message": "Error retrieving optimization jobs", "error": str(e)}


@router.put("/optimization_jobs/{job_id}")
def update_optimization_job(job_id: str, job: OptimizationJob):
    try:
        optimization_job_service.update_optimization_job(job_id, job)
        return {"message": "Optimization job updated successfully"}
    except Exception as e:
        return {"message": "Error updating optimization job", "error": str(e)}


@router.delete("/optimization_jobs/{job_id}")
def delete_optimization_job(job_id: str):
    try:
        optimization_job_service.delete_optimization_job(job_id)
        return {"message": "Optimization job deleted successfully"}
    except Exception as e:
        return {"message": "Error deleting optimization job", "error": str(e)}


app = APIRouter()
app.include_router(router)
