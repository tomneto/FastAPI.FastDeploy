from typing import Optional

from pydantic import BaseModel, Field
from api.docs.rules import username_rule_length, password_rule_length

class user(BaseModel):
	_uid: str = Field(default='', description='Boolean that indicates whether the mail has been validated or not.')
	name: str = Field(description='Valid name.')
	lastname: str = Field(description='Valid lastname.')
	username: str = Field(description='Valid username.', min_length=username_rule_length)
	password: str = Field(description='Valid password.', min_length=password_rule_length)
	mail: str = Field(description='Valid mail.')
	_mail_valid: bool = Field(default=False, description='Boolean that indicates whether the mail has been validated or not.')
	_two_factor_auth: Optional[bool] = Field(default=True, description='Boolean that indicates whether the two-factor authentication is enabled or not.')

