'''
Main API entrypoint. Contains the full application, including:
- running the server
- handling incoming requests
- delegating to API router
'''

from fastapi import FastAPI
# from app.api.routes import 

app = FastAPI()
