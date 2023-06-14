from fastapi import FastAPI, Depends
from fastapi_jwt_auth import AuthJWT

from api.router import route
from api.config import app_config
from api.middleware import enable_cors, enable_auth


class app(FastAPI):
	# applying basic api settings
	title = app_config().title

	def __init__(self):
		super().__init__()

		app = self

		# load up the authentication route
		enable_auth(app)

		# enable cors to work with mongodb and others that require connection over ethernet from Vercel to third party API's
		self.cors_state = enable_cors(self)

		# load the router obtained from the router package
		self.include_router(route)

		# execute initialization methods
		self.load_doc_settings()

	def load_doc_settings(self):
		if not app_config().show_doc:
			FastAPI(title='mailTo', docs_url=None, redoc_url=None)
		elif app_config().show_doc:
			FastAPI(title='mailTo')



