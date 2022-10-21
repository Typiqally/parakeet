"""Adds the controllers to the router"""
from fastapi import APIRouter
from api.controllers import version

router = APIRouter(
    prefix="/api"
)

router.include_router(version.router, tags=["version"])
