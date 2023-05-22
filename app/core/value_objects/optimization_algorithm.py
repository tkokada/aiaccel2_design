from enum import Enum


class OptimizationAlgorithm(str, Enum):
    RANDOM = "random"
    SOBOL = "sobol"
    GRID = "grid"
    NELDER_MEAD = "nelder_mead"
    TPE = "tpe"
