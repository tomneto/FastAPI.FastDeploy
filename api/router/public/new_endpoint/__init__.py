# external package's
import uuid
from fastapi import APIRouter, Response, Request
from starlette.responses import JSONResponse
from fastapi.param_functions import Query

# internal package's
from api.docs.descriptions import loadDescription

# load controller's and models here
from api.controllers.new_controller import find_one, find_many, insert_one, update_one, update_many, replace_one, \
	replace_many, delete_one, delete_many  # Example controller import
from .models import request as requestModels  # Example request model import
from .models import response as responseModels  # Example response model import

route = APIRouter()


@route.get("/new_endpoint", description=loadDescription("new_collection", 'get'), name="New Get", tags=["New Tag"],
		   response_model=responseModels.new_get_response_model)
async def new_get_endpoint(data: str = Query(description="New param description.")):
	try:

		condition = {'data': data}

		result = find_one(condition)

		if result is not None:
			result, status_code = result, 200

		else:
			result, status_code = {"message": "Data not found"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.post("/new_endpoint", description=loadDescription("new_collection", 'post'), name="New Post", tags=["New Tag"],
			response_model=responseModels.new_post_response_model)
async def new_post_endpoint(request: requestModels.new_post_request_model):
	try:

		result = insert_one(request)

		if result is not None:
			result, status_code = result, 200

		else:
			result, status_code = {"message": "This data already exists"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.put("/new_endpoint", description=loadDescription("new_collection", 'put'), name="New Put", tags=["New Tag"],
		   response_model=responseModels.new_put_response_model)
async def new_put_endpoint(request: requestModels.new_put_request_model):
	try:

		condition = {
			'data': request.data
		}

		update_transaction = {
			"$set": {'data': request.new_value}
		}

		result = update_one(condition, update_transaction)

		if result is not None:
			result, status_code = {"count": int(result)}, 200

		else:
			result, status_code = {"message": "Data has not been updated."}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.patch("/new_endpoint", description=loadDescription("new_collection", 'patch'), name="New Patch",
			 tags=["New Tag"], response_model=responseModels.new_patch_response_model)
async def new_patch_endpoint(request: requestModels.new_patch_request_model):
	try:

		condition = {
			'data': request.data
		}

		update_transaction = {
			"$set": {'data': request.new_value}
		}

		result = update_one(condition, update_transaction)

		if result is not None:
			result, status_code = {"count": int(result)}, 200

		else:
			result, status_code = {"message": "Data has not been updated."}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


@route.delete("/new_endpoint", description=loadDescription("new_collection", 'delete'), name="New Delete", tags=["New Tag"],
		   response_model=responseModels.new_delete_response_model)
async def new_put_endpoint(request: requestModels.new_delete_request_model):
	try:

		condition = {
			'data': request.data
		}

		result = delete_one(condition)

		if result is not None:
			result, status_code = {"count": int(result)}, 200

		else:
			result, status_code = {"message": "Data has not been deleted."}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)

