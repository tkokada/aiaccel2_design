import pytest
from app.core.entities.hyperparameter_definition import HyperparameterDefinition
from app.core.entities.optimization_job import OptimizationJob
from app.core.repositories.hyperparameter_definition_repository import (
    HyperparameterDefinitionRepository,
)
from app.core.repositories.optimization_job_repository import OptimizationJobRepository
from app.core.services.optimization_job_service import OptimizationJobService


class TestOptimizationJob:
    def test_create_optimization_job(self):
        repo = OptimizationJobRepository()
        service = OptimizationJobService(repo)
        job = OptimizationJob(name="Test Job", optimization_settings=None)
        created_job = service.create_optimization_job(job)
        assert created_job.name == "Test Job"

    def test_get_optimization_job(self):
        repo = OptimizationJobRepository()
        service = OptimizationJobService(repo)
        job = OptimizationJob(name="Test Job", optimization_settings=None)
        service.create_optimization_job(job)
        retrieved_job = service.get_optimization_job(job.id)
        assert retrieved_job.name == "Test Job"

    def test_update_optimization_job(self):
        repo = OptimizationJobRepository()
        service = OptimizationJobService(repo)
        job = OptimizationJob(name="Test Job", optimization_settings=None)
        service.create_optimization_job(job)
        job.name = "Updated Job"
        updated_job = service.update_optimization_job(job)
        assert updated_job.name == "Updated Job"

    def test_delete_optimization_job(self):
        repo = OptimizationJobRepository()
        service = OptimizationJobService(repo)
        job = OptimizationJob(name="Test Job", optimization_settings=None)
        service.create_optimization_job(job)
        service.delete_optimization_job(job)
        with pytest.raises(Exception):
            service.get_optimization_job(job.id)


class TestHyperparameterDefinition:
    def test_create_hyperparameter_definition(self):
        repo = HyperparameterDefinitionRepository()
        definition = HyperparameterDefinition(name="Test Definition", data_type="float")
        repo.create(definition)
        retrieved_definition = repo.get_by_id(definition.id)
        assert retrieved_definition.name == "Test Definition"

    def test_get_hyperparameter_definition(self):
        repo = HyperparameterDefinitionRepository()
        definition = HyperparameterDefinition(name="Test Definition", data_type="float")
        repo.create(definition)
        retrieved_definition = repo.get_by_id(definition.id)
        assert retrieved_definition.name == "Test Definition"

    def test_update_hyperparameter_definition(self):
        repo = HyperparameterDefinitionRepository()
        definition = HyperparameterDefinition(name="Test Definition", data_type="float")
        repo.create(definition)
        definition.name = "Updated Definition"
        repo.update(definition)
        updated_definition = repo.get_by_id(definition.id)
        assert updated_definition.name == "Updated Definition"

    def test_delete_hyperparameter_definition(self):
        repo = HyperparameterDefinitionRepository()
        definition = HyperparameterDefinition(name="Test Definition", data_type="float")
        repo.create(definition)
        repo.delete(definition)
        with pytest.raises(Exception):
            repo.get_by_id(definition.id)
