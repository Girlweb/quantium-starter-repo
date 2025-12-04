import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Read the processed data
df = pd.read_csv('output.csv')

# Convert date to datetime for proper sorting
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum sales across all regions
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Sort by date
daily_sales = daily_sales.sort_values('date')

# Create the line chart
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'}
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales ($)",
    hovermode='x unified',
    template='plotly_white',
    height=600
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    # Header
    html.H1(
        "Soul Foods - Pink Morsel Sales Dashboard",
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'marginTop': '20px',
            'fontFamily': 'Arial, sans-serif'
        }
    ),
    
    html.H3(
        "Analyzing Sales Before and After Price Increase (January 15, 2021)",
        style={
            'textAlign': 'center',
            'color': '#7f8c8d',
            'marginBottom': '30px',
            'fontFamily': 'Arial, sans-serif'
        }
    ),
    
    # Line chart
    dcc.Graph(
        id='sales-chart',
        figure=fig,
        style={'marginLeft': '50px', 'marginRight': '50px'}
    ),
    
    # Footer with insights
    html.Div([
        html.P(
            "📊 This visualization shows Pink Morsel sales trends over time.",
            style={
                'textAlign': 'center',
                'color': '#34495e',
                'marginTop': '30px',
                'fontSize': '16px'
            }
        ),
        html.P(
            "🔍 Look for the sales pattern change around January 15, 2021, when the price increase took effect.",
            style={
                'textAlign': 'center',
                'color': '#7f8c8d',
                'fontSize': '14px',
                'marginBottom': '40px'
            }
        )
    ])
], style={'backgroundColor': '#f8f9fa', 'minHeight': '100vh', 'paddingBottom': '20px'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
