from app.interfaces.api.optimization_job_api import router as optimization_job_router
from app.interfaces.cli.optimization_job_cli import cli as optimization_job_cli
from fastapi import FastAPI

app = FastAPI()

app.include_router(optimization_job_router)
optimization_job_cli()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
