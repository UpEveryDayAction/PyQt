import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go #いらんかも？
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Color:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Gold', 'MediumTurquoise', 'LightGreen']
        ],
        value='Green',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_color(color):
    # fig = go.Figure(
    #     data=go.Bar(y=[2, 3, 1], marker_color=color))
    # return fig


    df = pd.DataFrame({
        'time':[0, 0.5, 1.7, 3.3, 4.5, 6.1],
        'detect_count':[1,1,1,1,1,1],
        'direction':['right','left','right','left','right','right']
    })
    fig = px.pie(df, values='detect_count', names='direction',title='左右差')
    return fig
app.run_server(debug=True)