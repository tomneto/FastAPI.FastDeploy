# load the fastapi engine
import os

import pkg_resources
from fastapi import FastAPI, APIRouter, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# load the additional project content
from api.config import app_config
from api.middleware import enable_cors, enable_auth
from demo.home import path1
from docs.redoc import get_redoc_html

# load your endpoints here
from api.router.public import new_endpoint
## from api.router.private import

class App(FastAPI):

	def __init__(self):
		# applying basic api settings
		super().__init__(docs_url=None, redoc_url=None)

		self.title = app_config().title

		# load up the authentication route
		# enable_auth(app)

		# enable cors to work with mongodb and others that require connection over ethernet from Vercel to third party APIs
		self.cors_state = enable_cors(self)

		# execute initialization methods
		self.load_doc_settings()
		self.load_public_endpoints()
		self.load_private_endpoints()

	# set the documentation url based on the values obtained from the .env
	def load_doc_settings(self):
		if app_config().demo:
			self.path2 = os.path.abspath('../demo')
			self.path3 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'demo'))
			#self.mount('/demo', StaticFiles(directory='demo'), name="demo")


			#from demo.home import demo_route
			#self.include_router(demo_route)

		if app_config().show_doc:

			paths = [ path1, self.path2, self.path3 ]

			def print_all_packages():
				packages = []
				installed_packages = pkg_resources.working_set
				for package in installed_packages:
					packages.append(package)

				return packages

			doc_route = APIRouter()

			@doc_route.get("/test")
			async def test():
				result, status_code = {"packages": f"{print_all_packages()}", "paths": f"{paths}"}, 200
				return JSONResponse(content=result, status_code=status_code)


			@doc_route.get("/filesystem")
			async def filesystem():
				def read_filesystem(path):
					filesystem = []
					for root, dirs, files in os.walk(path):
						for file in files:
							file_path = os.path.join(root, file)
							file_info = {
								'path': file_path,
								'size': os.path.getsize(file_path),
								'created': os.path.getctime(file_path),
								'modified': os.path.getmtime(file_path)
							}
							filesystem.append(file_info)
						for directory in dirs:
							dir_path = os.path.join(root, directory)
							dir_info = {
								'path': dir_path,
								'created': os.path.getctime(dir_path),
								'modified': os.path.getmtime(dir_path)
							}
							filesystem.append(dir_info)
					return filesystem

				# Example usage
				filesystem_info = read_filesystem('/')
				result, status_code = {"fileSystem": f"{filesystem_info}"}, 200
				return JSONResponse(content=result, status_code=status_code)



			@doc_route.get(app_config.doc_url, include_in_schema=False)
			async def redoc_html(req: Request) -> HTMLResponse:
				root_path = req.scope.get("root_path", "").rstrip("/")
				openapi_url = root_path + self.openapi_url
				return get_redoc_html(
					openapi_url=openapi_url, title=self.title + " - ReDoc"
				)

			self.include_router(doc_route)

	# load your public endpoints here:
	def load_public_endpoints(self):
		self.include_router(new_endpoint.route)

	# load your private endpoints here:
	def load_private_endpoints(self):
		pass

app = App()
