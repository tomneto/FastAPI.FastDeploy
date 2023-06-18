from pydantic import BaseModel, validator
from typing import Optional


# GET - Base Model
class new_get_response_model(BaseModel):
	data: str


# POST - Base Model
class new_post_response_model(BaseModel):
	data: str


# PUT - Base Model
class new_put_response_model(BaseModel):
	count: int


# PATCH - Base Model
class new_patch_response_model(BaseModel):
	count: int
