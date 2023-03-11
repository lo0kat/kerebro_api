from fastapi import FastAPI
from .routers import words

description = "PostgreSQL CRUD API for Kerebro"

app = FastAPI(
    title="Kerebro CRUD API",
    description=description,
    version="1.0.0",
    contact={
        "name": "CHOMEL Louis",
    },
)
version = "v1" 
route_prefix= "/API/{}".format(version) 
app.include_router(words.router,prefix= route_prefix)
