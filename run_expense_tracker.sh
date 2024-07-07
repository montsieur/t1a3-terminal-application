# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

#!/bin/bash
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Run the main application
python3 src/main.py

# Deactivate the virtual environment
deactivate