import random
import secrets
import socket
import uuid

import names
from fastapi import Header
from pydantic import BaseModel, Field, validator
from typing import Optional, Annotated

from api.database.collections.device import device_collection
from api.docs.rules import username_rule_length, password_rule_length, product_id_length


class login(BaseModel):
	account: str = Field(description='Valid username or email.')
	password: str = Field(description='Valid password.', min_length=password_rule_length)
	product: Optional[str] = Field(default=None, description='id of product being signed, parse null for the public level access.', min_length=product_id_length, max_length=product_id_length)

class auth(BaseModel):
	access_token: Annotated[str | None, Header()] = None
	product: Annotated[str | None, Header()] = None
	uid: Annotated[str | None, Header()] = None
	dev: Annotated[str | None, Header()] = None
	#cookie_generated_refresh_token = Depends(generate_private_refresh)


class new_device(BaseModel):
	id: Optional[str] = Field(default='', description='Device ID.')
	user_id: Optional[str] = Field(default='', description='User ID.')
	device_fingerprint: str = Field(description='Device ID.')
	name: Optional[str] = Field(default=str(uuid.uuid4()), description='Device Name.')
	keep_alive: Optional[bool] = Field(default=False,
									   description='Trust device key, to keep the token alive for this device.')
	allowed: bool = Field(default=False,
						  description='Boolean value that indicates whether device is allowed for connection or not.')
	connected: Optional[bool] = Field(default=False,
									  description='Boolean value that indicates whether password is allowed for connection or not.')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.name = str(names.get_last_name() + f'_{random.randint(1,9999)}')

		if self.user_id != '':
			self.connected = True
		else:
			self.connected = False

		if self.connected:
			query = {
				'device_fingerprint': self.device_fingerprint,
				'user_id': self.user_id
			}
			device = device_collection().find_one(query)

			if device is not None:
				self.id = str(device['_id'])
				self.allowed = device_collection().find_one(query)['allowed']


class new_access(BaseModel):
	token = str(secrets.token_urlsafe(24))
	token_type: str
	user_id: str
	dev: str
	product: Optional[str] = None
	access_token: Optional[str] = None
