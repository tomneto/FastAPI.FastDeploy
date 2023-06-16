from typing import Annotated

import jwt
from fastapi import HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

async def authenticate(request):
    try:
        #
        print(request.headers['Authorization'])
    except Exception as e:
        print(e)


async def auth_middleware(request: Request, call_next):
    try:
        user = await authenticate(request)
        request.state.user = user  # Store the authenticated user object in the request state
        response = await call_next(request)
        return response
    except HTTPException as ex:
        response = JSONResponse(content={'status': 'Unauthorized'}, status_code=ex.status_code)
        return response
