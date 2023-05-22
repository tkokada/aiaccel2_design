from app.core.entities.hyperparameter import Hyperparameter
from app.core.value_objects.data_type import DataType
from app.core.value_objects.numeric_range import NumericRange


class HyperparameterFactory:
    @staticmethod
    def create(
        name: str,
        data_type: DataType,
        upper: NumericRange = None,
        lower: NumericRange = None,
        initial: float = None,
        choices: list = None,
    ) -> Hyperparameter:
        return Hyperparameter(
            name=name,
            data_type=data_type,
            upper=upper,
            lower=lower,
            initial=initial,
            choices=choices,
        )
