import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Read the processed data
df = pd.read_csv('output.csv')
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum sales across all regions
daily_sales = df.groupby('date')['sales'].sum().reset_index()
daily_sales = daily_sales.sort_values('date')

# Calculate sales by region for additional insights
regional_sales = df.groupby('region')['sales'].sum().reset_index()

# Identify the price change date
price_change_date = datetime(2021, 1, 15)

# Split data into before and after price change
before_change = daily_sales[daily_sales['date'] < price_change_date]
after_change = daily_sales[daily_sales['date'] >= price_change_date]

# Calculate average sales before and after
avg_before = before_change['sales'].mean()
avg_after = after_change['sales'].mean()
percent_change = ((avg_after - avg_before) / avg_before) * 100

# Create the main line chart with better styling
fig = go.Figure()

# Add trace for before price change
fig.add_trace(go.Scatter(
    x=before_change['date'],
    y=before_change['sales'],
    mode='lines',
    name='Before Price Change',
    line=dict(color='#3498db', width=3),
    fill='tozeroy',
    fillcolor='rgba(52, 152, 219, 0.1)',
    hovertemplate='<b>Date:</b> %{x|%Y-%m-%d}<br><b>Sales:</b> $%{y:,.0f}<extra></extra>'
))

# Add trace for after price change
fig.add_trace(go.Scatter(
    x=after_change['date'],
    y=after_change['sales'],
    mode='lines',
    name='After Price Change',
    line=dict(color='#e74c3c', width=3),
    fill='tozeroy',
    fillcolor='rgba(231, 76, 60, 0.1)',
    hovertemplate='<b>Date:</b> %{x|%Y-%m-%d}<br><b>Sales:</b> $%{y:,.0f}<extra></extra>'
))

# Add vertical line at price change
fig.add_vline(
    x=price_change_date.timestamp() * 1000,
    line_dash="dash",
    line_color="#95a5a6",
    line_width=2,
    annotation_text="Price Increase",
    annotation_position="top"
)

# Update layout with professional styling
fig.update_layout(
    title={
        'text': 'Pink Morsel Sales Trend Analysis',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 24, 'color': '#2c3e50', 'family': 'Arial Black'}
    },
    xaxis_title="Date",
    yaxis_title="Total Daily Sales ($)",
    hovermode='x unified',
    template='plotly_white',
    height=500,
    font=dict(family="Arial, sans-serif", size=12, color="#2c3e50"),
    plot_bgcolor='rgba(248, 249, 250, 0.8)',
    paper_bgcolor='white',
    xaxis=dict(
        showgrid=True,
        gridcolor='rgba(189, 195, 199, 0.3)',
        showline=True,
        linecolor='#bdc3c7'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='rgba(189, 195, 199, 0.3)',
        showline=True,
        linecolor='#bdc3c7'
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='#bdc3c7',
        borderwidth=1
    )
)

# Create regional breakdown chart
fig_regional = go.Figure(data=[
    go.Bar(
        x=regional_sales['region'],
        y=regional_sales['sales'],
        marker=dict(
            color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'],
            line=dict(color='#2c3e50', width=1.5)
        ),
        text=regional_sales['sales'].apply(lambda x: f'${x:,.0f}'),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Total Sales: $%{y:,.0f}<extra></extra>'
    )
])

fig_regional.update_layout(
    title={
        'text': 'Sales by Region',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial Black'}
    },
    xaxis_title="Region",
    yaxis_title="Total Sales ($)",
    template='plotly_white',
    height=400,
    plot_bgcolor='rgba(248, 249, 250, 0.8)',
    paper_bgcolor='white',
    font=dict(family="Arial, sans-serif", size=12, color="#2c3e50")
)

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Soul Foods Analytics"

# Define the app layout with cards and better structure
app.layout = html.Div([
    # Hero Section
    html.Div([
        html.Div([
            html.H1(
                "🍬 Soul Foods Analytics Dashboard",
                style={
                    'color': 'white',
                    'marginBottom': '10px',
                    'fontFamily': 'Arial Black, sans-serif',
                    'fontSize': '42px',
                    'textShadow': '2px 2px 4px rgba(0,0,0,0.3)'
                }
            ),
            html.H3(
                "Pink Morsel Sales Performance Analysis",
                style={
                    'color': '#ecf0f1',
                    'fontFamily': 'Arial, sans-serif',
                    'fontWeight': '300',
                    'fontSize': '20px'
                }
            )
        ], style={'textAlign': 'center', 'padding': '40px'})
    ], style={
        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'marginBottom': '30px',
        'borderRadius': '0 0 20px 20px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }),
    
    # Key Metrics Cards
    html.Div([
        # Card 1: Average Before
        html.Div([
            html.Div([
                html.H4("Before Price Change", style={'color': '#7f8c8d', 'marginBottom': '10px'}),
                html.H2(f"${avg_before:,.0f}", style={'color': '#3498db', 'margin': '0', 'fontSize': '36px'}),
                html.P("Average Daily Sales", style={'color': '#95a5a6', 'marginTop': '5px', 'fontSize': '14px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '25px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
                'border': '3px solid #3498db',
                'textAlign': 'center'
            })
        ], style={'flex': '1', 'margin': '0 10px'}),
        
        # Card 2: Average After
        html.Div([
            html.Div([
                html.H4("After Price Change", style={'color': '#7f8c8d', 'marginBottom': '10px'}),
                html.H2(f"${avg_after:,.0f}", style={'color': '#e74c3c', 'margin': '0', 'fontSize': '36px'}),
                html.P("Average Daily Sales", style={'color': '#95a5a6', 'marginTop': '5px', 'fontSize': '14px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '25px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
                'border': '3px solid #e74c3c',
                'textAlign': 'center'
            })
        ], style={'flex': '1', 'margin': '0 10px'}),
        
        # Card 3: Percent Change
        html.Div([
            html.Div([
                html.H4("Change", style={'color': '#7f8c8d', 'marginBottom': '10px'}),
                html.H2(
                    f"{percent_change:+.1f}%",
                    style={
                        'color': '#27ae60' if percent_change > 0 else '#e74c3c',
                        'margin': '0',
                        'fontSize': '36px'
                    }
                ),
                html.P("Impact of Price Increase", style={'color': '#95a5a6', 'marginTop': '5px', 'fontSize': '14px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '25px',
                'borderRadius': '15px',
                'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
                'border': f'3px solid {"#27ae60" if percent_change > 0 else "#e74c3c"}',
                'textAlign': 'center'
            })
        ], style={'flex': '1', 'margin': '0 10px'})
        
    ], style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'maxWidth': '1200px',
        'margin': '0 auto 40px auto',
        'padding': '0 20px'
    }),
    
    # Main Chart Card
    html.Div([
        dcc.Graph(
            id='sales-chart',
            figure=fig,
            config={'displayModeBar': True, 'displaylogo': False}
        )
    ], style={
        'backgroundColor': 'white',
        'padding': '30px',
        'borderRadius': '15px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
        'maxWidth': '1200px',
        'margin': '0 auto 30px auto'
    }),
    
    # Regional Chart Card
    html.Div([
        dcc.Graph(
            id='regional-chart',
            figure=fig_regional,
            config={'displayModeBar': True, 'displaylogo': False}
        )
    ], style={
        'backgroundColor': 'white',
        'padding': '30px',
        'borderRadius': '15px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
        'maxWidth': '1200px',
        'margin': '0 auto 30px auto'
    }),
    
    # Insights Section
    html.Div([
        html.H3("📊 Key Insights", style={'color': '#2c3e50', 'marginBottom': '20px'}),
        html.Ul([
            html.Li(
                f"The price increase on January 15, 2021 resulted in a {abs(percent_change):.1f}% "
                f"{'increase' if percent_change > 0 else 'decrease'} in average daily sales.",
                style={'marginBottom': '10px', 'fontSize': '16px'}
            ),
            html.Li(
                f"Average daily sales before: ${avg_before:,.0f}",
                style={'marginBottom': '10px', 'fontSize': '16px'}
            ),
            html.Li(
                f"Average daily sales after: ${avg_after:,.0f}",
                style={'marginBottom': '10px', 'fontSize': '16px'}
            ),
            html.Li(
                f"Total data points analyzed: {len(daily_sales):,} days across {len(regional_sales)} regions",
                style={'marginBottom': '10px', 'fontSize': '16px'}
            )
        ], style={'color': '#34495e', 'lineHeight': '1.6'})
    ], style={
        'backgroundColor': '#ecf0f1',
        'padding': '30px',
        'borderRadius': '15px',
        'maxWidth': '1200px',
        'margin': '0 auto 30px auto',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.05)'
    }),
    
    # Footer
    html.Div([
        html.P(
            "Soul Foods Data Analytics | Pink Morsel Product Line",
            style={'color': '#95a5a6', 'fontSize': '14px', 'textAlign': 'center', 'margin': '0'}
        )
    ], style={'padding': '20px'})
    
], style={
    'backgroundColor': '#f8f9fa',
    'minHeight': '100vh',
    'fontFamily': 'Arial, sans-serif'
})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
