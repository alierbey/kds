import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import dataGlobals

grafMakroDegiskenler =  html.Div([
                            html.H6("Makro Değişkenler", style={'text-align': 'center',"margin":"1rem"}),
                            dcc.Dropdown(id="graf2",
                                options=[{"label": x, "value": x} 
                                            for x in dataGlobals.df.columns[2:]],
                                value=dataGlobals.df.columns[2],
                                clearable=False,
                                ),
                            dcc.Graph(id="time-series-chart-graf2"),
                        ])

# Makro Değişkenler
@app.callback(
    Output("time-series-chart-graf2", "figure"), 
    [Input("graf2", "value")])
def display_time_series(graf2):
    fig = px.line(dataGlobals.df, x='Tarih', y=graf2, template="plotly_dark")
    fig.update_layout({
    "height":300,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig