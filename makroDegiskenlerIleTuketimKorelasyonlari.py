import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import scipy as sp
from app import app
import style
import dataGlobals




fig = go.Figure()


makroDegiskenlerIleTuketimKorelasyonlari = html.Div([
                            html.H6("Makro Değişkenler ile Tüketim Korelasyonları", style={'text-align': 'center',"margin":"1rem"}),
                               dcc.Dropdown(
                                    id="ticker",
                                    options=[{"label": x, "value": x} 
                                            for x in dataGlobals.df.columns[3:]],
                                    value=dataGlobals.df.columns[3],
                                    clearable=False,
                                ),
                                dcc.Graph(id="time-series-chart"),
                                ])



@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(dataGlobals.df['Tuketim'])
    y = np.array(dataGlobals.df[ticker])
    r = sp.stats.pearsonr(X, y) 
    
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = r[0],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': 'Tüketim & ' + ticker},
    
    gauge = {
        'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        # 'steps': [
        #     {'range': [-1, 0], 'color': 'gray'},
        #     {'range': [0, r[0]], 'color': 'royalblue'}]
        }))
    
    fig.update_layout({
        "height":300,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig