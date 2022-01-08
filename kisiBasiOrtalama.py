import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
from app import app


df = pd.read_excel("veri1_1.xlsx")

df['Tarih']=df['Tarih'].dt.year

df_tarih = df.groupby('Tarih')


grafKisiBasi =  html.Div([
                           html.H6("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),
                                    dcc.Dropdown(id="slct_year",
                                                options=[{"label": x, "value": x} 
                                                        for x in df_tarih.groups.keys()],
                                                clearable=False,
                                                multi=False,
                                                value=1986,
                                                style={'width': "40%"}
                                                ),

                                    dcc.Graph(id='mapp')
                        ])

@app.callback(
    Output('mapp', 'figure'),
    [Input('slct_year', 'value')]
)
def display_time_series(slct_year):
    fig = go.Figure(data=[go.Bar(
            x=df_tarih.get_group(slct_year).Periyot, y=df_tarih.get_group(slct_year).kbTuketim,
            textposition='auto'
        )])
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6,)
    
    fig.update_layout({
    "height":400,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig