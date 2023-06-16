import uuid

from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.requests import Request

from api.controllers.example import fetch_one, create, update, delete

from api.router.public.example.models import Post
from docs.descriptions import loadDescription

route = APIRouter()


@route.get("/example", description=loadDescription("example", 'get'), name="Get Example", tags=["Example Tag"])
async def exampleGet(uuid: uuid.UUID):
	try:

		result = fetch_one(uuid)

		if result:
			result, status_code = {"uuid": result}, 200

		else:
			result, status_code = {"message": "User not found"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.post("/example", description=loadDescription("example", 'post'), name="Post Example", tags=["Example Tag"])
async def examplePost(request: Post):
	try:

		result = create(request.user, request.password)

		if result is not None:
			result, status_code = {"uuid": result}, 200

		else:
			result, status_code = {"message": "This user already exists"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)
