import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
from scipy import stats
import scipy as sp
import random
from app import app
import style

##################  DESCRIPTIVE #####################
df = pd.read_excel("veri1.xlsx")

df['Tarih']=df['Tarih'].dt.year
df_tarih = df.groupby('Tarih')

fig = go.Figure()

pageDescriptive = html.Div(
    [
            html.H3("Descriptive"),
            html.Div([
                html.Div([
                    html.Div([
                            html.H6("Makro Değişkenler ile Tüketim Korelasyonları", style={'text-align': 'center',"margin":"1rem"}),
                               dcc.Dropdown(
                                    id="ticker",
                                    options=[{"label": x, "value": x} 
                                            for x in df.columns[3:]],
                                    value=df.columns[3],
                                    clearable=False,
                                ),
                                dcc.Graph(id="time-series-chart"),
                    ], style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem"})            
                ],className="col-xl-4"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.H6("Makro Değişkenler", style={'text-align': 'center',"margin":"1rem"}),
                            dcc.Dropdown(id="graf2",
                                options=[{"label": x, "value": x} 
                                            for x in df.columns[2:]],
                                value=df.columns[2],
                                clearable=False,
                                ),
                            dcc.Graph(id="time-series-chart-graf2"),
                        ])
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"margin":"1rem"})            
                ],className="col-xl-8",)
            ],className="row"),
            html.Hr(),
            html.Div([
                html.Div([
                    html.Div([
                                html.Div([
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
                                ],style = {"margin":"1rem"})
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
                ],className="col-xl-7",),
                html.Div([
                    html.Div([
                        html.Div([
                                html.H6("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center',"margin":"1rem"}),
                                html.P("Kategori:"),
                                dcc.Dropdown(
                                    id='slct_cat', 
                                    value='Teknik', 
                                    options=[{'value': x, 'label': x} 
                                            for x in ['Teknik', 'Cevre', 'Ekonomi']],
                                    clearable=False
                                ),
                                html.P("Tür"),
                                dcc.Dropdown(id='slct_tur', value='Uretim'),
                                html.Hr(),
                                dcc.Graph(id="pie-chart",figure=fig),
                            ],style = {"margin":"1rem"})
                    ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
                ],className="col-xl-5",)
            ],className="row"),
            html.Hr(),
    ], 
)


######### graf 1 #########

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[ticker])
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
######### graf 4


df2 = pd.read_excel("veri2.xlsx")

df_tur = df2.groupby(['Kategori','Tur'])
#print(df_tur.groups) 

yeap  = {"Teknik": [], "Cevre": [], "Ekonomi":[]}


for kat,tur in df_tur:
    if kat[0] == 'Teknik':
        yeap["Teknik"].append(kat[1])
    if kat[0] == 'Cevre':
        yeap["Cevre"].append(kat[1])
    if kat[0] == 'Ekonomi':
        yeap["Ekonomi"].append(kat[1])
        #print(kat[1])


###### pie #####


@app.callback(
    Output("time-series-chart2", "figure"), 
    [Input("graf2", "value")])
def display_time_series(graf2):
    #fig = px.line(df, x='Tarih', y=ticker, template="plotly_dark")
    X = np.array(df['Tuketim'])
    y = np.array(df[graf2])
    r = sp.stats.pearsonr(X, y) 

    fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = r[0]*100,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))
    fig.update_layout({
    "height":400,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig



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


@app.callback(
    Output("pie-chart", "figure"), 
    Input('slct_tur', 'value'),
    Input('slct_cat', 'value'),
)
def set_fig(slct_tur,slct_cat):

    df_cat = df2.groupby('Kategori')
    df_tur = df_cat.get_group(slct_cat)
    df_son = df_tur.groupby('Tur')
    df_filter = df_son.get_group(slct_tur)

    fig = px.pie(df_filter, values='Deger', names='Santral', template="plotly_dark")
    
    fig.update_layout({
    "height":400,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig

@app.callback(
    Output("slct_tur", "options"), 
    Input('slct_cat', 'value'),
)
def set_cat(x):
    
    return [{'label': i, 'value': i} for i in yeap[x]]

@app.callback(
    Output("time-series-chart-graf2", "figure"), 
    [Input("graf2", "value")])
def display_time_series(graf2):
    fig = px.line(df, x='Tarih', y=graf2, template="plotly_dark")
    fig.update_layout({
    "height":300,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig