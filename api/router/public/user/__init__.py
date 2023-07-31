# external package's
import uuid

from bson import ObjectId
from fastapi import APIRouter, Response, Request, HTTPException, Depends
from starlette.responses import JSONResponse
from fastapi.param_functions import Query

from api.controllers.auth import authorize
# internal package's
from api.docs.descriptions import loadDescription

# load controller's and models here
from api.controllers.user import find_one, insert_one, update_one # Example controller import
from .models import request as requestModels  # Example request model import
from .models import response as responseModels  # Example response model import

route = APIRouter()

@route.get("/user", description=loadDescription("user", 'get'), name="Get User", tags=["User"], response_model=responseModels.get_model)
async def user_get_endpoint(valid_token: str = Depends(authorize), uid: str = Query(description="User ID, obtained when using the access endpoint.")):
	try:
		condition = {'_id': ObjectId(uid)}
		result = find_one(condition)
		if result is not None:
			result, status_code = result, 200
		else:
			result, status_code = {"message": "User not found"}, 404
	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code, headers={'refresh-token': valid_token})

@route.post("/user", description=loadDescription("user", 'post'), name="Post User", tags=["User"], response_model=responseModels.post_model)
async def user_post_endpoint(request: requestModels.post_model):
	try:

		result = insert_one(request)

		if result is not None:
			result, status_code = {"uid": result}, 200

		else:
			result, status_code = {"message": "This data already exists"}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)

@route.patch("/user", description=loadDescription("user", 'patch'), name="Patch User", tags=["User"], response_model=responseModels.patch_model)
async def user_patch_endpoint(request: requestModels.patch_model):
	try:

		current_user = find_one({'_id': ObjectId(request.uid)}, password=True)

		changes = {}
		request_iter = request.__dict__

		for key in request_iter.keys():
			try:
				if request_iter[key] == current_user[key]:
					pass
				elif request_iter[key] != '':
					changes[key] = request_iter[key]
			except KeyError:
				print(KeyError)

		condition = {
			'_id': ObjectId(request.uid)
		}

		update_transaction = {
			"$set": changes
		}

		result = update_one(condition, update_transaction)

		if result is not None:
			result, status_code = {"count": int(result)}, 200

		else:
			result, status_code = {"message": "Data has not been updated."}, 404

	except Exception as e:
		result, status_code = {"message": e}, 500

	return JSONResponse(content=result, status_code=status_code)


