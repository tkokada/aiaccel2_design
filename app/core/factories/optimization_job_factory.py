from app.core.entities.optimization_job import OptimizationJob
from app.core.entities.optimization_settings import OptimizationSettings
from app.core.value_objects.name import Name


class OptimizationJobFactory:
    @staticmethod
    def create(
        name: Name, optimization_settings: OptimizationSettings
    ) -> OptimizationJob:
        _name = Name(value=name)
        return OptimizationJob(
            name=_name,
            optimization_settings=optimization_settings,
            # hyperparameter_definitions=optimization_settings.hyperparameter_definition_set,
            # execution_infrastructure_type=optimization_settings.infrastructure_type,
            # optimization_algorithm=optimization_settings.algorithm,
            # trial_jobs=optimization_settings.num_trials,
            # execution_command=optimization_settings.user_program,
        )
