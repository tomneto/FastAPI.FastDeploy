import uuid

fakeDb = []


def fetch_one(uuid: uuid.UUID):
	user = [e['uuid'] for e in fakeDb if str(e['uuid']) == str(uuid)]
	if user:
		return user[0]
	else:
		return None


def create(username: str, password: str):
	if username not in [e['username'] for e in fakeDb]:
		current_id = uuid.uuid4()
		new_user = {'password': password, 'username': username, 'uuid': str(current_id)}
		fakeDb.append(new_user)
		return str(current_id)
	else:
		return None


def update(username: str, password: str):
	set_pass = None
	for user in fakeDb:
		if user['username'] == username:
			user['password'] = password
			set_pass = True

	return set_pass


def delete(username: str, password: str):
	del_user = None
	for user in fakeDb:
		if user['username'] == username and password == user['password']:
			del user
			del_user = True

	return del_user
