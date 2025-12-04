#!/bin/bash

# CI Test Runner Script for Soul Foods Analytics Dashboard
# This script activates the virtual environment, runs tests, and returns appropriate exit codes

set -e  # Exit immediately if a command exits with a non-zero status

echo "======================================"
echo "Soul Foods - CI Test Runner"
echo "======================================"
echo ""

# Step 1: Activate virtual environment
echo " Step 1: Activating virtual environment..."
if [ -d "venv" ]; then
    source venv/bin/activate
    echo " Virtual environment activated"
else
    echo " ERROR: Virtual environment not found!"
    echo "Please create one with: python3 -m venv venv"
    exit 1
fi

echo ""

# Step 2: Verify dependencies
echo " Step 2: Checking dependencies..."
python -c "import dash, pandas, plotly" 2>/dev/null
if [ $? -eq 0 ]; then
    echo " All dependencies installed"
else
    echo " ERROR: Missing dependencies"
    echo "Installing dependencies..."
    pip install -q dash pandas plotly
fi

echo ""

# Step 3: Run tests
echo " Step 3: Running test suite..."
echo ""

# Run the tests and capture the exit code
python tests/test_app_simple.py

TEST_EXIT_CODE=$?

echo ""

# Step 4: Report results and return appropriate exit code
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "======================================"
    echo " SUCCESS: All tests passed!"
    echo "======================================"
    exit 0
else
    echo "======================================"
    echo " FAILURE: Tests failed!"
    echo "======================================"
    exit 1
fi
