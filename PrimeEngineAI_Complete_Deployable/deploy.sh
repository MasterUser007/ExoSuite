
#!/bin/bash
# Automated deployment script to run the app locally or on cloud instance

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting FastAPI server..."
uvicorn api.server:app --host 0.0.0.0 --port 8000
