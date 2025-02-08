#!/bin/bash

# setup.sh - Automates the environment setup for the resume project

# Step 1: Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed. Please install Python to continue."
    exit
fi

# Step 2: Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
else
    echo "Virtual environment already exists. Skipping creation."
fi

# Step 3: Activate the virtual environment
source venv/Scripts/activate

# Step 4: Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please create one with your dependencies."
    exit
fi

# Step 5: Confirmation message
echo "Setup complete! Virtual environment is ready and dependencies are installed."
echo "To activate the environment, use: source venv/Scripts/activate"
