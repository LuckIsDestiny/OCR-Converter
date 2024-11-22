#!/bin/bash

# Activate the virtual environment
source /appenv/bin/activate

# Run the FastAPI server with Uvicorn
uvicorn server:app --host 0.0.0.0 --port 8000