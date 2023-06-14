import server
from api.main import app
from api.config import app_config

if __name__ == "__main__":
	server.run("main:app")
