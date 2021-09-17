from fastapi import APIRouter
from starlette.requests import Request

chain_router = APIRouter(prefix='', tags=['Chain'])


@chain_router.get('/chain')
def get_chain(request: Request):
    return {

    }


@chain_router.post('/chain/verify')
def verify_chain():
    return {
    }
