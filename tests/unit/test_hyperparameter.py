import pytest
from app.core.entities.hyperparameter import Hyperparameter


class TestHyperparameter:
    def test_create_hyperparameter(self):
        hyperparameter = Hyperparameter(name="Test Hyperparameter", value=0.5)
        assert hyperparameter.name == "Test Hyperparameter"
        assert hyperparameter.value == 0.5

    def test_update_hyperparameter(self):
        hyperparameter = Hyperparameter(name="Test Hyperparameter", value=0.5)
        hyperparameter.value = 0.8
        assert hyperparameter.value == 0.8
