from api.database import connect
from api.config import app_config


# here we can define a mongo uri
db = connect(app_config.mongo_uri)

# it's also a good practice to keep a particular name to each collection to avoid conflicts when using multiple collections at the same time
def store_collection():
	return db.collection('store')


