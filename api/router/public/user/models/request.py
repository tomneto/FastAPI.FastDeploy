import re

from pydantic import BaseModel, validator, Field
from fastapi.param_functions import Query
from typing import Optional, Union, Any

from pydantic.fields import ModelField

from api.controllers.user import check_username, check_mail
from api.docs.rules import password_rule, username_rule, password_rule_length, username_rule_length, already_taken
from api.router.public.user.models import obj

# POST - Base Model
class post_model(obj.user):

	@validator("mail")
	def valid(cls, value):
		regExs = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
		if not re.search(regExs, value):
			raise ValueError("Please enter a valid email address")
		elif not check_mail(value):
			raise ValueError(already_taken('Email address'))
		else:
			return value

	@validator('username')
	def valid_username(cls, value):
		if len(value) >= username_rule_length:
			if not check_username(value):
				raise ValueError(already_taken('Username'))
			return value
		else:
			raise ValueError(
				f"Invalid username, {username_rule}")

	@validator('password')
	def valid_password(cls, value):

		if len(value) >= password_rule_length:
			return value
		else:
			raise ValueError(
				f"Invalid password, {password_rule}")


# PATCH - Base Model
class patch_model(obj.user):

	uid: str = Field(description='UserID')
	username: Optional[str] = Field(description='Valid username.', min_length=username_rule_length, default='')
	password: Optional[str] = Field(description='Valid password.', min_length=password_rule_length, default='')
	mail: Optional[str] = Field(description='Valid mail.', default='')
	name: Optional[str] = Field(description='Valid name.', default='')
	lastname: Optional[str] = Field(description='Valid lastname.', default='')

	@validator("mail")
	def valid(cls, value):
		regExs = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
		if not re.search(regExs, value):
			raise ValueError("Please enter a valid email address")
		elif not check_mail(value):
			raise ValueError(already_taken('Email address'))
		else:
			return value

	@validator('username')
	def valid_username(cls, value):
		if len(value) >= username_rule_length:
			if not check_username(value):
				raise ValueError(already_taken('Username'))
			return value
		else:
			raise ValueError(
				f"Invalid username, {username_rule}")

	@validator('password')
	def valid_password(cls, value):

		if len(value) >= password_rule_length:
			return value
		else:
			raise ValueError(
				f"Invalid password, {password_rule}")

