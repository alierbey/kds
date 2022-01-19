import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
pio.templates.default = "plotly_dark"
import pandas as pd
import dataGlobals

import numpy as np
import pandas as pd
import math
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import dataGlobals
import pandas as pd
import numpy as np
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
import dataGlobals
from app import app
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import dataGlobals

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


print("BULLLLETTTTTT ")




df = pd.read_excel("veri2.xlsx")
df1 = pd.read_excel('veri1.xlsx', 'Sheet2', date_parser=[0])

A = df["t1"] * 0.89
B = df1["Tuketim"]


# print(">>>>>>")
# print(type(B))
# print(B[dataGlobals.seciliTarih - 1980])



# print(A)
# print("----")
# print(A[0])

yil = dataGlobals.seciliTarih
agirlik = dataGlobals.w_son
valueR = 0 

def hesap():

    global yil
    global agirlik
    global valueR
    yil = dataGlobals.seciliTarih
    agirlik = dataGlobals.w_son

    print("BBBBBBBBBBBB ->>>>>>>>>>>>>>>>>><", yil)


    son = B[dataGlobals.seciliTarih - 1980]-A.sum()
    # A = np.array([113117.820, 56702.690, 88886.240, 29672.900, 240.900, 11363.200, 5257.630]) #ham
    #B = np.array([0.14836690050102408, 0.12445634863440393, 0.11705341989131955, 0.14570384986781632,
    #    0.10783025242823203, 0.15071984795678162, 0.20586938072042246]) #oransal


    mevcut = A.sum()
    print("mevcut XXXXXXXXX", mevcut)
    #son = 32949836.63435+35932290.865+34038540.09565+36045753.326299995+32201520.55695+32258251.7876+32314983.01825+33346955.2489+32428445.47955+32485176.7102+33517148.94085+33573880.1715
    ihtiyac = son-mevcut
    Yeni = ihtiyac*agirlik
    #Yeni = np.array([16416.183141990663, 13770.579593335323, 12951.47618399544, 16121.527617318358,
    #        11930.970898032086, 16676.527034238584, 22778.594456189573])
    valueR = Yeni + A
    print("------")
    print(valueR)



fig = html.Div([
        
        dcc.Dropdown(id="slct_year_yeni_bullet",
                    options=[{"label": x, "value": x} 
                            for x in range(2021,2040)],
                    clearable=False,
                    multi=False,
                    value=1987,
                    style={'display':'none','width': "40%","padding-left":60},
        ),
        dcc.Dropdown(id="slct_year_yeni5_bullet",
                    options=[{"label": x, "value": x} 
                            for x in range(2021,2040)],
                    clearable=False,
                    multi=False,
                    value=1987,
                    style={'display':'none','width': "40%","padding-left":60},
        ),
        

        dcc.Graph(id='pred_sc1_bullet'), 
        
    ])



@app.callback(
    Output('pred_sc1_bullet', 'figure'),
    [Input("slct_year_yeni_bullet", "value")]
)
def display1(value):
    print("girdi bullet")
    hesap()
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[0], #Son değer
        delta = {'reference': A[0], 'relative': True, 'valueformat':',.3%'}, #Mevcut miktar
        domain = {'x': [0.25, 1], 'y': [0.91, 0.98]},
        title = {'text': "Komur","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]}, #toplam uzunluk
            'steps': [
                {'range': [0, 113117.820], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
                ],
            'bar': {'color': "blue"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[1], #Son değer
        delta = {'reference': A[1],'relative': True, 'valueformat':',.3%'}, #Mevcut miktar
        domain = {'x': [0.25, 1], 'y': [0.77, 0.84]},
        title = {'text': "Doğalgaz","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]}, #toplam uzunluk
            'steps': [
                {'range': [0, 56702.690], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
                ],
            'bar': {'color': "blue"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[2], #Son değer
        delta = {'reference': A[2],'relative': True, 'valueformat':',.3%'}, #Mevcut miktar
        domain = {'x': [0.25, 1], 'y': [0.36, 0.43]},
        title = {'text': "Hidro","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]}, #toplam uzunluk
            'steps': [
                {'range': [0, 88886.240], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
                ],
            'bar': {'color': "blue"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[3], #Son değer
        delta = {'reference': A[3],'relative': True, 'valueformat':',.3%'}, #Mevcut miktar
        domain = {'x': [0.25, 1], 'y': [0.50, 0.57]},
        title = {'text': "Rüzgar","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]}, #toplam uzunluk
            'steps': [
                {'range': [0, 29672.900], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
                ],
            'bar': {'color': "blue"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[4], #Son değer
        delta = {'reference': A[4],'relative': True, 'valueformat':',.3%'}, #Mevcut miktar
        domain = {'x': [0.25, 1], 'y': [0.64, 0.71]},
        title = {'text': "Günes","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]}, #toplam uzunluk
            'steps': [
                {'range': [0, 240.900], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
                ],
            'bar': {'color': "blue"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[5],
        delta = {'reference': A[5],'relative': True, 'valueformat':',.3%'},
        domain = {'x': [0.25, 1], 'y': [0.22, 0.29]},
        title = {'text': "Jeotermal","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]},
            'steps': [
                {'range': [0, 11363.200], 'color': "gray"},
                ],
            'bar': {'color': "blue"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = valueR[6],
        delta = {'reference':A[6],'relative': True, 'valueformat':',.3%'},
        domain = {'x': [0.25, 1], 'y': [0.08, 0.15]},
        title = {'text' :"Biyokütle","font_size":14,},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200000]},
            'steps': [
                {'range': [0, 5257.630], 'color': "gray"},
                ],
            'bar': {'color': "blue"}}))
    fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

    fig.update_layout({
    "font_size":12,
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })

   

   

    return fig
