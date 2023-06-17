import sys
import inspect


def new_field_validator(value):
	minLen = 4
	if len(value) >= minLen:
		return value
	else:
		raise ValueError(f"Invalid {str(inspect.stack()[0][0].f_code.co_name).replace('_validator', '')}, username must contain at least {minLen} characters")

