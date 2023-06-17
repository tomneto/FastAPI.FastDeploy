# external package's
import uuid
from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.requests import Request

# internal package's
from docs.descriptions import loadDescription

# load controller's and models here
from api.controllers.new_controller import find_one, insert_one, update_one  # Example controller import
from api.router.public.new_endpoint.models import new_post_model  # Example model import

route = APIRouter()

@route.get("/new_collection", description=loadDescription("new_collection", 'get'), name="Get Example", tags=["Example Tag"])
async def new_get_endpoint(uuid: uuid.UUID):
	try:

		result = find_one(uuid)

		if result:
			result, status_code = {"uuid": result}, 200

		else:
			result, status_code = {"message": "User not found"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.post("/new_collection", description=loadDescription("new_collection", 'post'), name="Post Example", tags=["Example Tag"])
async def new_post_endpoint(request: new_post_model):
	try:

		result = insert_one(request.new_field)

		if result is not None:
			result, status_code = {"uuid": result}, 200

		else:
			result, status_code = {"message": "This user already exists"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)
