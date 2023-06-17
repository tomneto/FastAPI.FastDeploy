from pydantic import BaseModel, validator
from typing import Optional
from api.router.public.new_endpoint.validators import new_field_validator


class new_get_model(BaseModel):
	new_field: str

	@validator('new_field')
	def validate(cls, value):
		return new_field_validator(value)


class new_post_model(BaseModel):
	new_field: str

	@validator('new_field')
	def valid_name(cls, value):
		return new_field_validator(value)