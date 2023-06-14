import server
from api.app import app
from app.config import app_config

if __name__ == "__main__":
	server.run("api.app:app")
