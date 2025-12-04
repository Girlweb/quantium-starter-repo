"""
Test suite for Dash app components
Tests verify the presence of header, visualization, and region picker
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from dash.testing.application_runners import import_app


def test_header_presence(dash_duo):
    """
    Test 1: Verify that the header is present in the app
    """
    # Import the app
    app = import_app("app")
    
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the app to load
    dash_duo.wait_for_element("h1", timeout=10)
    
    # Check if header exists
    header = dash_duo.find_element("h1")
    
    # Assert header is present and has text
    assert header is not None, "Header element not found"
    assert header.text != "", "Header text is empty"
    
    print(f"✓ Header found with text: '{header.text}'")


def test_visualization_presence(dash_duo):
    """
    Test 2: Verify that the visualization (graph) is present in the app
    """
    # Import the app
    app = import_app("app")
    
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the graph component to load
    dash_duo.wait_for_element("#sales-graph", timeout=10)
    
    # Check if graph exists
    graph = dash_duo.find_element("#sales-graph")
    
    # Assert graph is present
    assert graph is not None, "Visualization/graph element not found"
    
    print("✓ Visualization found")


def test_region_picker_presence(dash_duo):
    """
    Test 3: Verify that the region picker (dropdown) is present in the app
    """
    # Import the app
    app = import_app("app")
    
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the dropdown component to load
    dash_duo.wait_for_element("#region-dropdown", timeout=10)
    
    # Check if dropdown exists
    dropdown = dash_duo.find_element("#region-dropdown")
    
    # Assert dropdown is present
    assert dropdown is not None, "Region picker/dropdown element not found"
    
    print("✓ Region picker found")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
