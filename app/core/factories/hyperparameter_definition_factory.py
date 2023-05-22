from app.core.entities.hyperparameter_definition import HyperparameterDefinition
from app.core.value_objects.choices import Choices
from app.core.value_objects.data_type import DataType
from app.core.value_objects.numeric_range import NumericRange


class HyperparameterDefinitionFactory:
    @staticmethod
    def create(
        name: str,
        data_type: DataType,
        upper: NumericRange = None,
        lower: NumericRange = None,
        initial: float = None,
        choices: Choices = None,
    ) -> HyperparameterDefinition:
        return HyperparameterDefinition(
            name=name,
            data_type=data_type,
            upper=upper,
            lower=lower,
            initial=initial,
            choices=choices,
        )
