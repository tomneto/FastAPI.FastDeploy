import json
from bson import json_util
from pymongo import UpdateMany

from api.database.collections.user import user_collection

def check_username(username):
	if find_one({'username': username}) is None:
		return True
	else:
		return False

def check_mail(mail):
	if find_one({'mail': mail}) is None:
		return True
	else:
		return False

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


# GET - Query Many Documents
def find_many(condition: any):
	try:
		# get the document from db
		documents = user_collection().find_many(condition)
		documents.pop("_id")  # remove the object id from documents
		return documents

	except Exception as e:
		# Handle the exception
		print("Error:", e)
		return None


# POST - Insert One
def insert_one(new_document: any):
	try:
		# create a new document here
		user_json = new_document.__dict__
		# create a new transaction and get the inserted id
		insert_result = user_collection().insert_one(user_json)
		inserted_id = insert_result.inserted_id

		# query the inserted document
		#inserted_transaction = user().find_one({"_id": inserted_id})
		#inserted_transaction.pop("_id")  # Remove the _id field

		return str(inserted_id)  ## IF FAILS json.loads(json_util.dumps(

	except Exception as e:
		# Handle the exception
		print("Error:", e)
		return None


# POST - Insert Many
def insert_many(new_documents: list):
	try:
		transactions = [
			{"data": doc.data} for doc in new_documents
		]
		insert_result = user_collection().insert_many(transactions)
		inserted_ids = insert_result.inserted_ids
		inserted_documents = user_collection().find({"_id": {"$in": inserted_ids}})
		inserted_documents = [
			doc.pop("_id") and doc for doc in inserted_documents
		]

		return inserted_documents
	except Exception as e:
		print("Error:", e)
		return None


# PUT - Replace One
def replace_one(data: any, updated_document: any):
	try:
		update_result = user_collection().replace_one(data, updated_document)
		return update_result.modified_count
	except Exception as e:
		print("Error:", e)
		return None


# PUT - Replace Many
def replace_many(condition: dict, replacement_documents: list):
	try:
		requests = [
			UpdateMany(condition, {"$replaceRoot": {"newRoot": doc}}) for doc in replacement_documents
		]
		update_result = user_collection().bulk_write(requests)
		return update_result.modified_count
	except Exception as e:
		print("Error:", e)
		return None


# PATCH - Update One
def update_one(condition: any, updated_fields: any):
	try:
		update_result = user_collection().update_one(condition, updated_fields)
		return update_result.modified_count
	except Exception as e:
		print("Error:", e)
		return None


# PATCH - Update Many
def update_many(condition: dict, updated_fields: dict):
	try:
		update_result = user_collection().update_many(condition, updated_fields)
		return update_result.modified_count
	except Exception as e:
		print("Error:", e)
		return None


# DELETE - Delete One
def delete_one(condition: dict):
	try:
		delete_result = user_collection().delete_one(condition)
		return delete_result.deleted_count
	except Exception as e:
		print("Error:", e)
		return None


# DELETE - Delete Many
def delete_many(condition: dict):
	try:
		delete_result = user_collection().delete_many(condition)
		return delete_result.deleted_count
	except Exception as e:
		print("Error:", e)
		return None
