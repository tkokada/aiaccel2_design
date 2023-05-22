from app.core.entities.hyperparameter_definition import HyperparameterDefinition


class HyperparameterDefinitionRepository:
    def __init__(self):
        self.hyperparameter_definitions: list[HyperparameterDefinition] = []

    def create(
        self, hyperparameter_definition: HyperparameterDefinition
    ) -> HyperparameterDefinition:
        self.hyperparameter_definitions.append(hyperparameter_definition)
        return hyperparameter_definition

    def get_all(self) -> list[HyperparameterDefinition]:
        return self.hyperparameter_definitions

    def get_by_id(self, definition_id: str) -> HyperparameterDefinition:
        for definition in self.hyperparameter_definitions:
            if definition.id == definition_id:
                return definition
        return None

    def update(
        self, hyperparameter_definition: HyperparameterDefinition
    ) -> HyperparameterDefinition:
        for i, definition in enumerate(self.hyperparameter_definitions):
            if definition.id == hyperparameter_definition.id:
                self.hyperparameter_definitions[i] = hyperparameter_definition
                return hyperparameter_definition
        return None

    def delete(self, definition_id: str) -> bool:
        for i, definition in enumerate(self.hyperparameter_definitions):
            if definition.id == definition_id:
                del self.hyperparameter_definitions[i]
                return True
        return False
