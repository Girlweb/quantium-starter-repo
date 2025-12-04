"""
Simple unit tests for Soul Foods Dash App (no browser needed)
"""
import sys
sys.path.insert(0, '.')

from app import app
import pandas as pd


def test_app_exists():
    """Test 001: Verify the app object exists"""
    assert app is not None, "App object should exist"
    assert hasattr(app, 'layout'), "App should have a layout"
    print("✅ TEST PASSED: App exists and has layout")


def test_data_loaded():
    """Test 002: Verify output.csv data exists and is valid"""
    df = pd.read_csv('output.csv')
    
    # Check required columns exist
    required_columns = ['sales', 'date', 'region']
    for col in required_columns:
        assert col in df.columns, f"Column '{col}' should exist in output.csv"
    
    # Check data is not empty
    assert len(df) > 0, "Data should not be empty"
    
    # Check regions
    expected_regions = {'north', 'south', 'east', 'west'}
    actual_regions = set(df['region'].unique())
    assert actual_regions == expected_regions, f"Expected regions {expected_regions}, got {actual_regions}"
    
    print(f"✅ TEST PASSED: Data loaded correctly with {len(df)} rows")


def test_layout_components():
    """Test 003: Verify key layout components exist"""
    layout_str = str(app.layout)
    
    # Check for key text in layout
    assert 'Soul Foods' in layout_str, "Layout should contain 'Soul Foods' header"
    assert 'region-filter' in layout_str, "Layout should contain region filter"
    assert 'sales-chart' in layout_str, "Layout should contain sales chart"
    
    print("✅ TEST PASSED: All required components present in layout")


def test_callback_exists():
    """Test 004: Verify callback is registered"""
    # Check if callback is registered
    assert len(app.callback_map) > 0, "App should have at least one callback"
    
    # Check if our specific callback exists
    callback_ids = [str(cb) for cb in app.callback_map.values()]
    has_sales_chart_callback = any('sales-chart' in cb for cb in callback_ids)
    
    assert has_sales_chart_callback, "Should have callback for sales-chart"
    print("✅ TEST PASSED: Callbacks are registered correctly")


if __name__ == '__main__':
    test_app_exists()
    test_data_loaded()
    test_layout_components()
    test_callback_exists()
    print("\n🎉 All tests passed!")
