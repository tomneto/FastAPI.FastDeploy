from pydantic import BaseModel, validator
from fastapi.param_functions import Query
from typing import Optional
from .validators import new_field_validator


# POST - Base Model
class new_post_request_model(BaseModel):
	data: str = Query(description='New post description.')

	@validator('data')
	def valid_name(cls, value):
		return new_field_validator(value)


# PUT - Base Model
class new_put_request_model(BaseModel):
	data: str = Query(description='New put description.')
	new_value: str = Query(description='New put description.')

	@validator('data')
	def valid_name(cls, value):
		return new_field_validator(value)

	@validator('new_value')
	def valid_value(cls, value):
		return new_field_validator(value)


# PATCH - Base Model
class new_patch_request_model(BaseModel):
	data: str = Query(description='New patch description.')
	new_value: str = Query(description='New patch description.')

	@validator('data')
	def valid_name(cls, value):
		return new_field_validator(value)

	@validator('new_value')
	def valid_value(cls, value):
		return new_field_validator(value)


# DELETE - Base Model
class new_delete_request_model(BaseModel):
	data: str = Query(description='New delete description.')

	@validator('data')
	def valid_name(cls, value):
		return new_field_validator(value)
