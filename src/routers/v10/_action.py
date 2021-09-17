from fastapi import APIRouter
from starlette.requests import Request

action_router = APIRouter(prefix='', tags=['Action'])


@action_router.post('/action')
def add_action():
    return {
    }


@action_router.get('/action')
def get_action(request: Request):
    return {

    }


@action_router.post('/action/verify')
def verify_action(request: Request):
    return {

    }


