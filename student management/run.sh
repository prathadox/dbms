#!/bin/bash
# Student Management System - Run Script

cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Run Flask app
python main.py

