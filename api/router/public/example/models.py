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


class Put(BaseModel):
	user: str
	new_user: str
	password: str
	new_password: str
	confirmation: str

	@validator('user')
	def valid_user(cls, value):
		return username(value)

	@validator('new_user')
	def valid_new_user(cls, value):
		return username(value)


	@validator('password')
	def valid_password(cls, value):
		return password(value)

	@validator('new_password')
	def valid_new_password(cls, value):
		return password(value)



class Patch(BaseModel):
	user: str
	new_user: Optional[str]
	password: str
	new_password: Optional[str]
	confirmation: str

	@validator('user')
	def valid_user(cls, value):
		return username(value)

	@validator('new_user')
	def valid_new_user(cls, value):
		return username(value)

	@validator('password')
	def valid_password(cls, value):
		return password(value)

	@validator('new_password')
	def valid_new_password(cls, value):
		return password(value)

class Delete(BaseModel):
	user: str
	password: str
	confirmation: str

	@validator('user')
	def valid_name(cls, value):
		return username(value)

	@validator('password')
	def valid_password(cls, value):
		return password(value)
