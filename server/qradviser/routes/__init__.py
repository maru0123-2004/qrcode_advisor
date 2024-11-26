from fastapi import APIRouter

router=APIRouter()

from .auth import router as auth_router
router.include_router(auth_router, prefix="/auth")

from .search import router as search_router
router.include_router(search_router, prefix="/search")

from .checkstop import router as checkstop_router
router.include_router(checkstop_router, prefix="/checkstop")