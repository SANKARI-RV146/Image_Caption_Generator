#!/bin/bash

echo "Starting deployment of VisionaryLens - Image Caption Generator..."
cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "Dependencies installed."

echo "Starting the application..."
streamlit run app.py

deactivate
echo "Application stopped and virtual environment deactivated."
