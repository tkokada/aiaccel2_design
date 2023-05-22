from pydantic import BaseModel


class HyperparameterValues(BaseModel):
    values: dict[str, float]
