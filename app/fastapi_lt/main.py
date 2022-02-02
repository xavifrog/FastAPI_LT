from fastapi import FastAPI
import os

try:
    app_env = os.environ["APP_ENV"]
except KeyError:
    app_env = "Develop"


if app_env == "Production":
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
elif app_env == "Develop":
    app = FastAPI()
else:
    print("Unexpected error: unexpected env state")
    raise




@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
