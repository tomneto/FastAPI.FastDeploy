def username(value):
	minLen = 4
	if len(value) >= minLen:
		return value
	else:
		raise ValueError(f"Invalid username, username must contain at least {minLen} characters")


def password(value):
	minLen = 12
	if len(value) >= minLen:
		return value
	else:
		raise ValueError(f"Invalid password, password must contain at least {minLen} characters")
