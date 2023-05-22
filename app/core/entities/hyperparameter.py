from app.core.value_objects import Choices, Initial
from app.core.value_objects.data_type import DataType
from app.core.value_objects.name import Name
from app.core.value_objects.numeric_range import NumericRange
from app.utilities.uuid_generator import generate_uuid
from pydantic import UUID4, BaseModel, Field


class Hyperparameter(BaseModel):
    id: UUID4 = Field(default_factory=generate_uuid)
    name: Name
    data_type: DataType
    numeric_range: NumericRange
    initial: Initial
    choices: Choices
