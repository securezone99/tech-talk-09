import sys
import os

# Add project root to the Python path
# This allows the app to be run from the app directory, e.g., for local development.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import logging
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cursor.app.controllers import health_controller
from cursor.app.controllers import markdown_controller

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
app = FastAPI(docs_url="/docs")

# Add CORS middleware
origins = [
    "*",  # Allows all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers#
app.include_router(health_controller.router, prefix="/health", tags=["health"])
app.include_router(markdown_controller.router, prefix="/markdown", tags=["markdown"])