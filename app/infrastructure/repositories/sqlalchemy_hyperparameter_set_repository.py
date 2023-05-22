from app.core.entities.hyperparameter_set import HyperparameterSet
from app.core.repositories.hyperparameter_set_repository import (
    HyperparameterSetRepository,
)
from app.infrastructure.models import HyperparameterSetModel
from sqlalchemy.orm import Session


class SQLAlchemyHyperparameterSetRepository(HyperparameterSetRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, hyperparameter_set: HyperparameterSet):
        hyperparameter_set_model = HyperparameterSetModel(
            id=hyperparameter_set.id,
            name=hyperparameter_set.name,
            hyperparameters=hyperparameter_set.hyperparameters,
        )
        self.session.add(hyperparameter_set_model)
        self.session.commit()

    def get(self, hyperparameter_set_id: str) -> HyperparameterSet:
        hyperparameter_set_model = (
            self.session.query(HyperparameterSetModel)
            .filter(HyperparameterSetModel.id == hyperparameter_set_id)
            .first()
        )
        if hyperparameter_set_model:
            return HyperparameterSet(
                name=hyperparameter_set_model.name,
                hyperparameters=hyperparameter_set_model.hyperparameters,
            )
        return None

    def delete(self, hyperparameter_set_id: str):
        self.session.query(HyperparameterSetModel).filter(
            HyperparameterSetModel.id == hyperparameter_set_id
        ).delete()
        self.session.commit()
