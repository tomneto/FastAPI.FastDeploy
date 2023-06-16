from typing import Annotated

from fastapi import APIRouter, Request
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse, JSONResponse

security = HTTPBasic()

route = APIRouter()

# change the following variable for the data source you want to store the authenticated users
authenticated_users = {}

@route.get("/login")
async def login(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    authenticated = False
    try:
        user = credentials.username
        password = credentials.password

        # your authentication goes here
        if user == 'root' and password == 'root':
            authenticated_users[user] = True
            authenticated = True

    except Exception as e:
        print(e)
        authenticated = False

    if not authenticated:
        raise HTTPException(status_code=401, detail="Unauthorized")

    else:
        user = {"username": "john.doe"}
        return user

# Sign-out endpoint
@route.get("/logout")
def logout(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username

    # Check if the user is authenticated
    if username in authenticated_users:
        del authenticated_users[username]

        return RedirectResponse('/')
    else:
        return JSONResponse(content={"message": "Logout successful"}, headers={'Authorization': ''})

