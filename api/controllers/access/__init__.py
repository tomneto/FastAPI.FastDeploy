import secrets

from api.database.collections.access import access_collection
from api.database.collections.device import device_collection
from api.database.collections.store import store_collection
from api.database.collections.user import user_collection
from bson.objectid import ObjectId

def generate_access_register(access):
	def query_available_product():

		available_product_condition = {
			'user_id': access.user_id,
			'product': access.product,
			'available': True
		}

		if store_collection().find_one(available_product_condition) is not None:
			return True
		else:
			return False

	def query_valid_access_token():
		valid_access_token_condition = {
			'user_id': access.user_id,
			'product': access.product,
			'token': access.access_token,
			'token_type': 'access'
		}

		if access_collection().find_one(valid_access_token_condition) is not None:
			return True
		else:
			return False

	try:
		if query_available_product():
			print('product is available')
			current_token_condition = {
				'user_id': access.user_id,
				'dev': access.dev,
				'product': access.product,
				'$or': [
					{
						'access_token': access.access_token,
						'token_type': 'refresh'
					},
					{
						'access_token': access.access_token,
						'token_type': access.token_type
					}
				]
			}
			current_token = access_collection().find_one(current_token_condition)

			# store a token if not generated yet
			if current_token is None and access.access_token is None:
				print('creating new token')
				insert_result = access_collection().insert_one(access.__dict__)
				inserted_id = insert_result.inserted_id
				result = access.token

			elif access.token_type == 'access' and current_token['token_type'] == 'access':
				result = current_token['token']

			elif access.token_type == 'refresh' and query_valid_access_token():
				new_data = access.__dict__
				new_data['token'] = str(secrets.token_urlsafe(24))
				print(f'Attempt to store refresh token: {new_data}')

				upsert_condition = {'dev': access.dev, 'token_type': access.token_type, 'user_id': access.user_id,
									'access_token': access.access_token}

				insert_result = access_collection().update_one(upsert_condition, {'$set': new_data}, upsert=True)

				result = new_data['token']
				new_data = None

			else:
				result = f'Failed to store refresh token to access request: {access.__dict__}'
				print(result)
				raise Exception(result)

			return result

		else:
			raise Exception('Product unavailable.')

	except Exception as e:
		raise e


def check_password(user: any):
	condition = {
		"$or": [
			{"username": user.account},
			{"mail": user.account}
		],
		"password": {"$regex": user.password, "$options": "i"}
	}

	client_ = find_one(condition)

	if client_ is None:
		return ''
	else:
		return str(client_['_id'])


def query_device(user_id, device_id):
	device = {
		"user_id": user_id,
		"_id": ObjectId(device_id)
	}

	print('Looking for device: ', device)
	try:
		return device_collection().find_one(device)

	except Exception as e:
		# Handle the exception
		print("Error:", e)
		return None


# POST - Insert One
def log_device(device: any):
	device = device.__dict__
	del device['id']

	insert_result = device_collection().insert_one(device)
	inserted_id = insert_result.inserted_id

	return insert_result


# GET - Query One Document
def find_one(condition: any, password: bool = False):
	try:
		# get the document from db
		document = user_collection().find_one(condition)
		document['_id'] = str(document['_id'])
		if not password:
			document.pop('password')
		return document

	except Exception as e:
		# handle the exception
		print("Error:", e)
		return None
