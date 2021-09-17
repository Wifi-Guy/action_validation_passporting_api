from starlette.requests import Request
from uuid import uuid4


async def add_uuid_to_request(request: Request, call_next):
    correlation_id = uuid4() if 'X-Correlation-id' not in request.headers else request.headers["X-Correlation-id"]
    request.state.correlation_id = str(correlation_id)
    response = await call_next(request)
    response.headers["X-Correlation-id"] = str(correlation_id)
    return response
