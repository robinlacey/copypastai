#!/bin/bash

# Check if an argument is provided
if [ "$1" != "" ]; then
    ARG="$1"
else
    ARG=""
fi

# Check whether directory contains /venv
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Check if requirements are satisfied or not
pip freeze | grep -q -F -f requirements.txt || REQUIREMENTS_MISSING="true"

if [ "$REQUIREMENTS_MISSING" = "true" ]; then
    echo "Requirements missing. Installing..."
    pip install -r requirements.txt
else
    echo "All requirements are satisfied."
fi

# Run python script as root
sudo python main.py $ARG

# Deactivate virtual environment
deactivate

echo "Script executed successfully."
