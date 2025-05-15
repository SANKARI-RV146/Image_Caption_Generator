#!/bin/bash

echo "Starting Streamlit Cloud Deployment for VisionaryLens..."
cd "$(dirname "$0")"

if [ ! -f "requirements.txt" ]; then
    echo "Generating requirements.txt..."
    pip freeze > requirements.txt
fi

if [ ! -f "Procfile" ]; then
    echo "Creating Procfile for Streamlit Cloud..."
    echo "web: streamlit run app.py" > Procfile
fi

if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit for Streamlit Cloud deployment"
fi

echo "Please push to GitHub and connect to Streamlit Cloud."
