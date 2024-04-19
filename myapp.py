import dash
from dash import dcc, html
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mi Primer Panel Dash'),
    dcc.Slider(
        id='my-slider',
        min=0,
        max=1000,
        step=1,
        value=500,
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')]
)
def update_graph(value):
    data = np.random.randn(value)
    fig = go.Figure(data=[go.Histogram(x=data)])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

 


'''http://127.0.0.1:8050/'''