from fastapi import FastAPI

from orbitalscope.api.routes.health import router as health_router


def create_app() -> FastAPI:
    """Create and configure the OrbitalScope API."""

    application = FastAPI(
        title="OrbitalScope API",
        description="Backend and data platform for ingesting, validating, "
        "processing, and exploring public space-object data.",
        version="0.1.0",
    )

    application.include_router(health_router)

    return application


app = create_app()
