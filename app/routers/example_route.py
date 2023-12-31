from fastapi import APIRouter, Depends

from app.schemes.auth import TokenData
from app.services.auth import checking_credentials

router = APIRouter(prefix='/test_rout', tags=['Test Data'])


@router.post('/create/', response_model=TokenData, deprecated=True)
async def data_types(
    auth_user: checking_credentials = Depends(),
):
    """im ok, im not alcoholic"""
    return auth_user
