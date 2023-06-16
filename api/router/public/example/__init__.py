import uuid

from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.requests import Request

from api.controllers.example import fetch_one, create, update, delete

from api.router.public.example.models import Post, Put, Patch, Delete
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


@route.put("/example", description=loadDescription("example", 'put'), name="Put Example", tags=["Example Tag"])
async def examplePut(request: Put):
	try:
		result = update(request.user, request.password, request.newpassword)
		if result is not None:
			result, status_code = {"uuid": result}, 200
		else:
			result, status_code = {"message": "Failed on user update"}, 404
	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.patch("/example", description=loadDescription("example", 'patch'), name="Patch Example", tags=["Example Tag"])
async def examplePatch(request: Patch):
	try:
		result = update(request.user, request.password)
		if result is not None:
			result, status_code = {"uuid": result}, 200
		else:
			result, status_code = {"message": "Failed on user patch"}, 404
	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.delete("/example", description=loadDescription("example", 'delete'), name="Delete Example", tags=["Example Tag"])
async def exampleDelete(request: Delete):
	try:
		result = delete(request.user, request.password)
		if result is not None:
			result, status_code = {"uuid": result}, 200
		else:
			result, status_code = {"message": "Failed on user delete"}, 404
	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)

