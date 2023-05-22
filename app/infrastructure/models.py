from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HyperparameterDefinitionModel(Base):
    __tablename__ = "hyperparameter_definition"

    id = Column(String, primary_key=True)
    name = Column(String)
    data_type = Column(String)
    upper = Column(JSON)
    lower = Column(JSON)
    initial = Column(JSON)
    choices = Column(JSON)


class HyperparameterSetModel(Base):
    __tablename__ = "hyperparameter_set"

    id = Column(String, primary_key=True)
    name = Column(String)
    hyperparameters = Column(JSON)


class OptimizationJobModel(Base):
    __tablename__ = "optimization_job"

    id = Column(String, primary_key=True)
    name = Column(String)
    optimization_settings = Column(JSON)
    creation_date = Column(JSON)
    updated_date = Column(JSON)


class OptimizationSettingsModel(Base):
    __tablename__ = "optimization_settings"

    id = Column(String, primary_key=True)
    infrastructure_type = Column(String)
    algorithm = Column(String)
    num_trials = Column(Integer)
    hyperparameter_definition_set = Column(JSON)
    seed = Column(Integer)
    user_program = Column(String)


class TrialJobModel(Base):
    __tablename__ = "trial_job"

    id = Column(String, primary_key=True)
    hyperparameter_set = Column(JSON)
    execution_command = Column(String)
    status = Column(String)
    result = Column(JSON)
