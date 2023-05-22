from app.core.entities.optimization_settings import OptimizationSettings


class OptimizationSettingsRepository:
    def __init__(self):
        self.optimization_settings: list[OptimizationSettings] = []

    def create(
        self, optimization_settings: OptimizationSettings
    ) -> OptimizationSettings:
        self.optimization_settings.append(optimization_settings)
        return optimization_settings

    def get_all(self) -> list[OptimizationSettings]:
        return self.optimization_settings

    def get_by_id(self, settings_id: str) -> OptimizationSettings:
        for settings in self.optimization_settings:
            if settings.id == settings_id:
                return settings
        return None

    def update(
        self, optimization_settings: OptimizationSettings
    ) -> OptimizationSettings:
        for i, settings in enumerate(self.optimization_settings):
            if settings.id == optimization_settings.id:
                self.optimization_settings[i] = optimization_settings
                return optimization_settings
        return None

    def delete(self, settings_id: str) -> bool:
        for i, settings in enumerate(self.optimization_settings):
            if settings.id == settings_id:
                del self.optimization_settings[i]
                return True
        return False
