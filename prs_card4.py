# -*- coding: utf-8 -*-

import plotly.graph_objects as go
import dataGlobals as dataGlobal
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.io as pio
from app import app
from prs_card2 import yeniHesap
pio.templates.default = "seaborn"
import style
import dataGlobals

import math



entr_ilk = 0 
entr_son = 0 


def hesap():
    sy = dataGlobals.seciliTarih #seçillen yıl bilgisi
    # w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1]) #hesaplanan ağırlıklar
    w_son = dataGlobals.w_son

    df = pd.read_excel("veri2.xlsx")
    mevcut = np.array(df.t1) #kaynaklara göre dağılım (mevcut durum)
    t_mevcut = sum(mevcut) #mevcut üretim toplamı
    o_mevcut = np.array(mevcut/t_mevcut)

    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    deger = round(a*sy*sy+b*sy+c)
    t_ihtiyac = deger - t_mevcut 
    ihtiyac = t_ihtiyac*w_son #kaynaklara göre dağılım (eklenen kısım)

    tum = mevcut + ihtiyac #kaynaklara göre dağılım (son durum)
    o_tum = np.array(tum/deger)


    k= -1/np.log(7)
    global entr_ilk
    global entr_son
    entr_ilk =  k*sum(o_mevcut*np.log(o_mevcut))
    entr_son =  k*sum(o_tum*np.log(o_tum))






# fig.add_trace(go.Indicator(
#     mode = "number",
#     value = entr_ilk,
#     title = {"text": "2020 Entropi Değeri"},
#     domain = {'x': [0, 1], 'y': [0, 0.5]}))

# fig.add_trace(go.Indicator(
#     mode = "number",
#     value = entr_son,
#     title = {"text": " " +str(sy)+  " Entropi Değeri"},
#     domain = {'x': [0, 1], 'y': [0.5, 1]}))

# fig.update_layout({
#     "height": 500,
#     "font_color":"white",
#     "plot_bgcolor": "rgba(0, 0, 0, 0)",
#     "paper_bgcolor": "rgba(0, 0, 0, 0)",
# })

fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni4",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
     dcc.Dropdown(id="slct_year_yeni4_1",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
    html.H6("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),
    dcc.Graph(id='prs_card4'),
    dcc.Graph(id='prs_card4_1')
])



@app.callback(
    Output('prs_card4', 'figure'),
    [Input("slct_year_yeni4", "value")]
)
def display(value):
    hesap()
    print("****Girdim5****")
    fig = go.Figure(go.Indicator(
    mode = "number",
    value = entr_ilk,
    title = {"text": "2020 Entropi Değeri"},
    domain = {'x': [0, 1], 'y': [0, 0.5]}))
    fig.update_layout({
        "height": 300,
        "font_color":"white",
        "title_font_family":"Times New Roman",
        "title_font_color":"red",
        "legend_title_font_color":"green",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
    return fig


@app.callback(
    Output('prs_card4_1', 'figure'),
    [Input("slct_year_yeni4_1", "value")]
)
def display(value):
    hesap()
    print("****Girdim6****")
    fig = go.Figure(go.Indicator(
    mode = "number",
    value = entr_son,
    title = {"text": " " +str(dataGlobals.seciliTarih)+  " Entropi Değeri"},
    domain = {'x': [0, 1], 'y': [0.5, 1]}))
    fig.update_layout({
        "height": 300,
        "font_color":"white",
        "title_font_family":"Times New Roman",
        "title_font_color":"red",
        "legend_title_font_color":"green",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
    return fig


# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter