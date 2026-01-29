#!/bin/bash
# Wrapper script to start ProCAST AI Automation presentation app

# Change to app directory
cd /home/exedev/clawd/turbocharger-procast-demo

# Check if virtual environment exists, create if not
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install fastapi uvicorn jinja2
else
    source .venv/bin/activate
fi

# Start the app on port 8080
exec uvicorn src.app:app --host 127.0.0.1 --port 8080