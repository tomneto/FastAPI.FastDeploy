# external package's
import string
from typing import Optional, Annotated, Union

from bson import ObjectId
from fastapi import APIRouter, Request, Depends, Response, Header
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.param_functions import Query, Cookie

from api.constants import available_products
from api.controllers.auth import get_fingerprint
# internal package's
from api.docs.descriptions import loadDescription

# load controller's and models here
from api.controllers.access import log_device, check_password, generate_access_register, query_device
from .models import request as requestModels  # Example request model import
from .models import response as responseModels  # Example response model import
from .models.obj import new_device, new_access

route = APIRouter()

@route.post("/auth", description=loadDescription("access", 'post'), name="Generate Refresh Token",
			tags=["User Authentication"], response_model=responseModels.auth)
async def auth(
		response: Response,
		request: Request,
		access_token: Annotated[str | None, Header()],
		uid: Annotated[str | None, Header()],
		dev: Annotated[str | None, Header()],
		product: Annotated[str | None, Header()] = None
):
	user_device = query_device(user_id=uid, device_id=dev)
	result = None

	try:
		if user_device is not None and user_device['allowed']:

			access = new_access(
				user_id=user_device['user_id'],
				dev=str(user_device['_id']),
				access_token=access_token,
				token_type='refresh',
				product=product
			)

			result = generate_access_register(access)

			message, code = {'refresh_token': result}, 200

		else:
			raise Exception('Invalid device.')

	except Exception as e:
		message, code = {'error': str(e)}, 500

	response = JSONResponse(content=message, status_code=code, headers={'refresh-token': str(result)})

	if result is not None:
		response.set_cookie('refresh_token', result)

	return response

@route.post("/login", description=loadDescription("access", 'post'), name="Login User (Generate access_token)", tags=["User Authentication"],
			response_model=responseModels.login)
async def login(
		body: requestModels.login,
		request: Request,
		fingerprint: str = Depends(get_fingerprint),
):
	headers = None
	user_device = None

	try:

		user_device = new_device(user_id=check_password(body), device_fingerprint=str(fingerprint), user=body)

		if user_device.id == '':
			device = log_device(user_device)
			message, status_code = {"message": "Device created waiting for mail validation."}, 201

		else:
			message, status_code = {"message": "Device not allowed, please check your email."}, 401

	except Exception as e:
		message, status_code = {'error': str(e)}, 500

	if user_device is not None and user_device.allowed:
		access = new_access(user_id=user_device.user_id, dev=user_device.id, token_type='access', product=body.product)

		try:
			result = generate_access_register(access)
			path = f'/auth'

			headers = {
				'access_token': result,
				'uid': access.user_id,
				'dev': user_device.id
			}

			status_code = 200
			message = {'message': 'Login Successfully'}

		except Exception as e:
			message = {'error': str(e)}

	response = JSONResponse(content=message, headers=headers, status_code=status_code)

	return response
