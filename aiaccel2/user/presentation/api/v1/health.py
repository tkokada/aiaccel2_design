from fastapi import APIRouter

from aiaccel2.user.presentation.api.v1.health_response import HealthResponse

health_router = APIRouter()


@health_router.get("/api/v1/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status=True)
