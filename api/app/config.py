from dotenv import load_dotenv
import os

load_dotenv()

class app_config:
	# dev settings
	debug = bool(os.getenv("DEBUG", default=True))

	# api settings
	title = str(os.getenv("TITLE"))
	port = int(os.getenv("PORT"))
	host = str(os.getenv("HOST"))

	# doc settings
	show_doc = bool(os.getenv("ENABLE_DOCUMENTATION"))

