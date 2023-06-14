from api.router.example_route import route
from api.router.userAuth import route


@route.get("/")
async def main():
    return {"message": "Initialized!"}
