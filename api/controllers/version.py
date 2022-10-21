"""Version controller"""
from fastapi import APIRouter
from api.version import __version__

router = APIRouter()


@router.get("/version")
async def get_version():
    """Get version"""

    return {
        "version": __version__
    }
