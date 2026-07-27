from fastapi import APIRouter

from orbitalscope.schemas.health import HealthResponse

router = APIRouter(tags=["system"])


@router.get(
    "/health",
    summary="Health check endpoint",
)
def health_check() -> HealthResponse:
    """
    Health check endpoint to verify the service is running.
    """
    return HealthResponse()
