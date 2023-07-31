from pydantic import BaseModel, validator
from typing import Optional

from api.router.public.user.models import obj


# GET - Base Model
class get_model(BaseModel):
	uid: str


# POST - Base Model
class post_model(BaseModel):
	uid: str


# PATCH - Base Model
class patch_model(BaseModel):
	count: int

