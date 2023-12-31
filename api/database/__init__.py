# external modules
import os
import certifi
import importlib
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# internal modules
from api.config import app_config

collections = [collection for collection in os.listdir(os.path.join(os.path.dirname(__file__), 'collections'))]


def load_indexes(collection_name):
	try:
		module_name = f"api.database.collections.{collection_name}"
		collection_module = __import__(module_name, fromlist=['indexes'])
		collection_indexes = getattr(collection_module, 'indexes')
		return collection_indexes.get_indexes()
	except ImportError:
		return None


def set_indexes(collection, collection_name):
	indexes = load_indexes(collection_name)
	if indexes is not None:
		for index in indexes:
			try:
				collection.create_indexes([index])
			except:
				pass


class connect:

	def __init__(self, uri: str):

		if app_config.debug:
			self.mongo_client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
		else:
			self.mongo_client = MongoClient(uri, server_api=ServerApi('1'))

		self.db = self.mongo_client.database

		try:
			self.mongo_client.admin.command('ping')
			print("Pinged your deployment. You successfully connected to MongoDB!")


		except Exception as e:
			raise e

	def collection(self, collection_name):
		collection = self.db.__getattr__(collection_name)
		# load the indexes from the respective collection folder
		set_indexes(collection, collection_name)

		return collection
