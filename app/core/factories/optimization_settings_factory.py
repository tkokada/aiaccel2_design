import yaml
from app.core.entities.optimization_settings import OptimizationSettings
from app.core.value_objects.execution_infrastructure_type import (
    ExecutionInfrastructureType,
)
from app.core.value_objects.optimization_algorithm import OptimizationAlgorithm


class OptimizationSettingsFactory:
    @staticmethod
    def create(
        infrastructure_type: ExecutionInfrastructureType,
        algorithm: OptimizationAlgorithm,
        num_trials: int,
        hyperparameter_definition_set: list,
        seed: int = None,
        user_program: str = None,
    ) -> OptimizationSettings:
        return OptimizationSettings(
            infrastructure_type=infrastructure_type,
            algorithm=algorithm,
            num_trials=num_trials,
            hyperparameter_definition_set=hyperparameter_definition_set,
            seed=seed,
            user_program=user_program,
        )

    @staticmethod
    def create_from_yaml(file_path: str) -> OptimizationSettings:
        with open(file_path, "r") as file:
            settings = yaml.safe_load(file)
        return OptimizationSettings(**settings)

    @staticmethod
    def save_to_yaml(settings: OptimizationSettings, file_path: str):
        with open(file_path, "w") as file:
            yaml.safe_dump(settings.__dict__, file)
