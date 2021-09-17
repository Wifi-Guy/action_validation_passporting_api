from logging.config import fileConfig
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from middleware import add_uuid_to_request
from routers import v10

app = FastAPI(title='Action Validation Passport API', debug=False)

app.add_middleware(BaseHTTPMiddleware, dispatch=add_uuid_to_request)

api_v1_router = APIRouter(prefix='/api/v1')

fileConfig('../logging.ini', disable_existing_loggers=False)


@app.get('/', include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url='/docs')


api_v1_router.include_router(v10.action_router)
api_v1_router.include_router(v10.chain_router)

api_v1_router.include_router(v10.healthcheck_router)

app.include_router(api_v1_router)
