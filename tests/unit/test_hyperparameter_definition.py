import pytest
from app.core.entities.hyperparameter_definition import HyperparameterDefinition
from app.core.repositories.hyperparameter_definition_repository import (
    HyperparameterDefinitionRepository,
)


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
