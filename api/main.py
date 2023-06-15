from fastapi import FastAPI

from api.router import route
from api.config import app_config
from api.middleware import enable_cors, enable_auth


class App(FastAPI):


	def __init__(self):
		# applying basic api settings
		super().__init__()
		self.title = app_config().title
		app = self

		# load up the authentication route
		#enable_auth(app)

		# enable cors to work with mongodb and others that require connection over ethernet from Vercel to third party API's
		#self.cors_state = enable_cors(self)

		# load the router obtained from the router package
		#self.include_router(route)

		# execute initialization methods
		#self.load_doc_settings()

	def load_doc_settings(self):
		if not app_config().show_doc:
			self.docs_url = None
			self.redoc_url = None
		elif app_config().show_doc:
			pass

app = App()
