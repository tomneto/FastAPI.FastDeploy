from dotenv import load_dotenv
import os

load_dotenv('example.env')


class app_config:
	# dev settings
	debug = bool(os.getenv("DEBUG", default=True))

	# api settings
	title = str(os.getenv("TITLE"))
	port = int(os.getenv("PORT"))
	host = str(os.getenv("HOST"))

	# mongo db settings
	mongo_uri = bool(os.getenv("MONGO_URI"))  # in order to add more than a database to your project, please duplicate this line and set another .env variable.

	# doc settings
	show_doc = bool(os.getenv("ENABLE_DOCUMENTATION"))

