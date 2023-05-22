from abc import ABC, abstractmethod

from app.core.entities.optimization_job import OptimizationJob


class OptimizationJobRepository(ABC):
    @abstractmethod
    def save(self, optimization_job: OptimizationJob):
        raise NotImplementedError

    @abstractmethod
    def get(self, optimization_job_id: str) -> OptimizationJob:
        raise NotImplementedError

    @abstractmethod
    def delete(self, optimization_job_id: str):
        raise NotImplementedError
