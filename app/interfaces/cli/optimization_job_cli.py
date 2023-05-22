import click
from app.core.factories.hyperparameter_definition_factory import (
    HyperparameterDefinitionFactory,
)
from app.core.factories.optimization_job_factory import OptimizationJobFactory
from app.core.factories.optimization_settings_factory import OptimizationSettingsFactory
from app.core.repositories.hyperparameter_definition_repository import (
    HyperparameterDefinitionRepository,
)
from app.core.repositories.optimization_settings_repository import (
    OptimizationSettingsRepository,
)
from app.core.repositories.trial_job_repository import TrialJobRepository
from app.core.services.optimization_job_service import OptimizationJobService
from app.infrastructure.databases.database import get_session
from app.infrastructure.repositories.sqlalchemy_optimization_job_repository import (
    SQLAlchemyOptimizationJobRepository,
)

session = get_session()
optimization_job_repository = SQLAlchemyOptimizationJobRepository(session=session)
hyperparameter_definition_repository = HyperparameterDefinitionRepository()
optimization_settings_repository = OptimizationSettingsRepository()
trial_job_repository = TrialJobRepository()
optimization_job_service = OptimizationJobService(
    optimization_job_repository,
    hyperparameter_definition_repository,
    optimization_settings_repository,
    trial_job_repository,
)
optimization_settings_factory = OptimizationSettingsFactory()
hyperparameter_definition_factory = HyperparameterDefinitionFactory()
optimization_job_factory = OptimizationJobFactory()


@click.command()
@click.option("--name", required=True, help="The name of the optimization job")
@click.option(
    "--settings-file",
    required=True,
    help="The path to the YAML file containing optimization settings",
)
def create_optimization_job(name, settings_file):
    # try:
    optimization_settings = optimization_settings_factory.create_from_yaml(
        settings_file
    )
    job = optimization_job_factory.create(
        name=name,
        optimization_settings=optimization_settings,
    )
    optimization_job_service.create_optimization_job(job)
    click.echo("Optimization job created successfully")
    # except Exception as e:
    #    click.echo(f"Failed to create optimization job: {str(e)}")


@click.command()
def get_optimization_jobs():
    try:
        jobs = optimization_job_service.get_optimization_jobs()
        for job in jobs:
            click.echo(f"Name: {job.name}, ID: {job.id}")
    except Exception as e:
        click.echo(f"Failed to retrieve optimization jobs: {str(e)}")


@click.command()
@click.argument("job_id")
@click.option("--name", help="The new name of the optimization job")
def update_optimization_job(job_id, name):
    try:
        job = optimization_job_service.get_optimization_job(job_id)
        if not job:
            raise Exception("Optimization job not found")
        if name:
            job.name = name
        optimization_job_service.update_optimization_job(job)
        click.echo("Optimization job updated successfully")
    except Exception as e:
        click.echo(f"Failed to update optimization job: {str(e)}")


@click.command()
@click.argument("job_id")
def delete_optimization_job(job_id):
    try:
        job = optimization_job_service.get_optimization_job(job_id)
        if not job:
            raise Exception("Optimization job not found")
        optimization_job_service.delete_optimization_job(job)
        click.echo("Optimization job deleted successfully")
    except Exception as e:
        click.echo(f"Failed to delete optimization job: {str(e)}")


@click.group()
def cli():
    pass


cli.add_command(create_optimization_job)
cli.add_command(get_optimization_jobs)
cli.add_command(update_optimization_job)
cli.add_command(delete_optimization_job)

if __name__ == "__main__":
    cli()
