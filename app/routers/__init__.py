from fastapi import APIRouter

from app.routers.auth import router as auth_router
from app.routers.example_route import router as example_router

router = APIRouter(prefix='/v1')

router.include_router(auth_router)
router.include_router(example_router)
