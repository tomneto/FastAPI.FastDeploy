from api.database.collections.new_collection import new_collection

import uuid


def find_one(uid: uuid.UUID):

	try:
		# Find the document with the given uid
		document = new_collection.find_one({'uid': str(uid)})

		if document:
			# Convert the document to JSON format
			jsonData = {
				'new_field': document['new_field'],
			}

			return jsonData
		else:
			return None

	except Exception as e:
		# Handle the exception
		print("Error:", e)
		return False


def insert_one(new_value: str):

	try:
		transaction = {
			'new_field': new_value,
		}
		new_collection.insert_one(transaction)

		return str(transaction)

	except Exception as e:
		# Handle the exception
		print("Error:", e)
		return False


def update_one(old: str, new_value: str):
	try:
		transaction = {
			'new_field': new_value,
		}
		new_collection.update_one(
			{'new_value': old},  # here we can set the filter to the query
			{
				'$set': {'new_value': new_value}  # here we set the values to apply
			}
		)

		return str(transaction)

	except Exception as e:
		# Handle the exception
		print("Error:", e)
		return False



