from pydantic import BaseModel


class NumericRange(BaseModel):
    upper: float
    lower: float
