from fastapi import APIRouter
from starlette.requests import Request

healthcheck_router = APIRouter(prefix='', tags=['Healthcheck'])


@healthcheck_router.get('/healthcheck')
def get_healthcheck():

    return {
        'status': True
    }


@healthcheck_router.get('/appinfo')
def get_appinfo(request: Request):
    return {
        'correlation_id': request.state.correlation_id
    }
