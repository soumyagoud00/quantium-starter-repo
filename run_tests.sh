#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest

# Return appropriate exit code
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
