from fastapi import APIRouter

route = APIRouter()

@route.get("/example")
async def example_route():
    return {"message": "This is an example route"}
