from pydantic import BaseModel, validator
from typing import Optional
from api.router.public.example.validators import username, password


class Get(BaseModel):
	user: str

	@validator('user')
	def validate(cls, value):
		return username(value)


class Post(BaseModel):
	user: str
	password: str

	@validator('user')
	def valid_name(cls, value):
		return username(value)

	@validator('password')
	def valid_password(cls, value):
		return password(value)
