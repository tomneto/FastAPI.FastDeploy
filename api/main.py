from fastapi import FastAPI

from api.router import public
from api.config import app_config
from api.middleware import enable_cors, enable_auth


class App(FastAPI):

	def __init__(self):
		# applying basic api settings
		super().__init__()
		self.title = app_config().title
		app = self

		# load up the authentication route
		enable_auth(app)

		# enable cors to work with mongodb and others that require connection over ethernet from Vercel to third party APIs
		self.cors_state = enable_cors(self)

		# execute initialization methods
		self.load_doc_settings()
		self.load_public_endpoints()

	# set the documentation url based on the values obtained from the .env
	def load_doc_settings(self):
		if app_config().show_doc:
			pass
		elif not app_config().show_doc:
			self.docs_url = None
			self.redoc_url = None

	# load your public endpoints here:
	def load_public_endpoints(self):
		self.include_router(public.new_endpoint.route)


app = App()
