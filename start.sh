#!/bin/bash
# Donation Inventory API Startup Script

echo "🚀 Starting Donation Inventory API..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import fastapi" &> /dev/null; then
    echo "Installing dependencies..."
    pip install fastapi uvicorn sqlalchemy
fi

echo "Starting server on http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo "Press Ctrl+C to stop the server"
echo ""

# Start the FastAPI application
uvicorn main:app --reload --host 0.0.0.0 --port 8000