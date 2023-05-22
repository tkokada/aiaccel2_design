from app.core.entities.hyperparameter_set import HyperparameterSet


class HyperparameterSetRepository:
    def __init__(self):
        self.hyperparameter_sets: list[HyperparameterSet] = []

    def create(self, hyperparameter_set: HyperparameterSet) -> HyperparameterSet:
        self.hyperparameter_sets.append(hyperparameter_set)
        return hyperparameter_set

    def get_all(self) -> list[HyperparameterSet]:
        return self.hyperparameter_sets

    def get_by_id(self, set_id: str) -> HyperparameterSet:
        for set in self.hyperparameter_sets:
            if set.id == set_id:
                return set
        return None

    def update(self, hyperparameter_set: HyperparameterSet) -> HyperparameterSet:
        for i, set in enumerate(self.hyperparameter_sets):
            if set.id == hyperparameter_set.id:
                self.hyperparameter_sets[i] = hyperparameter_set
                return hyperparameter_set
        return None

    def delete(self, set_id: str) -> bool:
        for i, set in enumerate(self.hyperparameter_sets):
            if set.id == set_id:
                del self.hyperparameter_sets[i]
                return True
        return False
