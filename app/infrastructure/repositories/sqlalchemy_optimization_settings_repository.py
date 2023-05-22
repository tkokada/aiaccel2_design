from app.core.entities.optimization_settings import OptimizationSettings
from app.core.repositories.optimization_settings_repository import (
    OptimizationSettingsRepository,
)
from app.infrastructure.models import OptimizationSettingsModel
from sqlalchemy.orm import Session


class SQLAlchemyOptimizationSettingsRepository(OptimizationSettingsRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, optimization_settings: OptimizationSettings):
        optimization_settings_model = OptimizationSettingsModel(
            id=optimization_settings.id,
            infrastructure_type=optimization_settings.infrastructure_type,
            algorithm=optimization_settings.algorithm,
            num_trials=optimization_settings.num_trials,
            hyperparameter_definition_set=optimization_settings.hyperparameter_definition_set,
            seed=optimization_settings.seed,
            user_program=optimization_settings.user_program,
        )
        self.session.add(optimization_settings_model)
        self.session.commit()

    def get(self, optimization_settings_id: str) -> OptimizationSettings:
        optimization_settings_model = (
            self.session.query(OptimizationSettingsModel)
            .filter(OptimizationSettingsModel.id == optimization_settings_id)
            .first()
        )
        if optimization_settings_model:
            return OptimizationSettings(
                infrastructure_type=optimization_settings_model.infrastructure_type,
                algorithm=optimization_settings_model.algorithm,
                num_trials=optimization_settings_model.num_trials,
                hyperparameter_definition_set=optimization_settings_model.hyperparameter_definition_set,
                seed=optimization_settings_model.seed,
                user_program=optimization_settings_model.user_program,
            )
        return None

    def delete(self, optimization_settings_id: str):
        self.session.query(OptimizationSettingsModel).filter(
            OptimizationSettingsModel.id == optimization_settings_id
        ).delete()
        self.session.commit()
