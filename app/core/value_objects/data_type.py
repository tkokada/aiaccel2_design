from enum import Enum


class DataType(str, Enum):
    INT = "int"
    FLOAT = "float"
    CATEGORICAL = "categorical"
    ORDINAL = "ordinal"
