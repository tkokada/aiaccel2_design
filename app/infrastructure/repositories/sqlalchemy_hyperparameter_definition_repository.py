from app.core.entities.hyperparameter_definition import HyperparameterDefinition
from app.core.repositories.hyperparameter_definition_repository import (
    HyperparameterDefinitionRepository,
)
from app.infrastructure.models import HyperparameterDefinitionModel
from sqlalchemy.orm import Session


class SQLAlchemyHyperparameterDefinitionRepository(HyperparameterDefinitionRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, hyperparameter_definition: HyperparameterDefinition):
        hyperparameter_definition_model = HyperparameterDefinitionModel(
            id=hyperparameter_definition.id,
            name=hyperparameter_definition.name,
            data_type=hyperparameter_definition.data_type.value,
            upper=hyperparameter_definition.upper.value
            if hyperparameter_definition.upper
            else None,
            lower=hyperparameter_definition.lower.value
            if hyperparameter_definition.lower
            else None,
            initial=hyperparameter_definition.initial.value
            if hyperparameter_definition.initial
            else None,
            choices=hyperparameter_definition.choices.value
            if hyperparameter_definition.choices
            else None,
        )
        self.session.add(hyperparameter_definition_model)
        self.session.commit()

    def get(self, hyperparameter_definition_id: str) -> HyperparameterDefinition:
        hyperparameter_definition_model = (
            self.session.query(HyperparameterDefinitionModel)
            .filter(HyperparameterDefinitionModel.id == hyperparameter_definition_id)
            .first()
        )
        if hyperparameter_definition_model:
            return HyperparameterDefinition(
                name=hyperparameter_definition_model.name,
                data_type=hyperparameter_definition_model.data_type,
                upper=hyperparameter_definition_model.upper,
                lower=hyperparameter_definition_model.lower,
                initial=hyperparameter_definition_model.initial,
                choices=hyperparameter_definition_model.choices,
            )
        return None

    def delete(self, hyperparameter_definition_id: str):
        self.session.query(HyperparameterDefinitionModel).filter(
            HyperparameterDefinitionModel.id == hyperparameter_definition_id
        ).delete()
        self.session.commit()
