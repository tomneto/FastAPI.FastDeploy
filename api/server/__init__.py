import uvicorn
from api.config import app_config

def run(app: any):
    try:
        uvicorn.run(app, host=app_config().host, port=app_config().port, reload=app_config().debug)
    except (ValueError, KeyError, Exception) as e:
        print(e)
