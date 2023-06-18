from dotenv import load_dotenv
import os

load_dotenv()

class app_config:
	# dev settings
	debug = bool(os.environ.get("DEBUG", default=True))

	# api settings
	title = str(os.environ.get("TITLE"))
	port = int(os.environ.get("PORT"))
	host = str(os.environ.get("HOST"))

	# mongo db settings
	mongo_uri = str(os.environ.get("MONGO_URI"))  # in order to add more than a database to your project, please duplicate this line and set another .env variable.

	# doc settings
	show_doc = bool(os.environ.get("ENABLE_DOCUMENTATION"))
	doc_url = str(os.environ.get("DOCUMENTATION_URL", default="/docs"))
