# -*- coding: utf-8 -*-
"""
Nüfus Tahmin
"""
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

import math
 
#kullanıcı tarafından girilen yıl verisi gelecek

date_train = 0
nufus_trainx = 0
date_test = 0
nufust_pre_testx = 0
date_test = 0
nufus_testx = 0
pre_yil = 0
nufust_prex = 0

def hesap():

    global date_train
    global nufus_trainx
    global date_test
    global nufust_pre_testx
    global date_test
    global nufus_testx
    global pre_yil
    global nufust_prex
    
    yil = dataGlobals.seciliTarih

    # Datayı Yükleyelim
    df = pd.read_excel('veri1.xlsx', 'Sheet1', date_parser=[0])
    dft = pd.read_excel('veri1.xlsx', 'Sheet2', date_parser=[0])
    print(df.info())

    t = [i for i in range(1980, 2021)]
    Tarih = np.array(t)
    #Tarih sütununun index'e Alınması
    df.index = df.Tarih
    dft.index = dft.Tarih
    df.drop(columns=['Tarih', 'Tuketim', 'GSD', 'GSTL', 'SUE'], inplace=True)
    dft.drop(columns=['Tarih', 'Tuketim', 'GSD', 'GSTL', 'SUE'], inplace=True)

    nufus_data = df['Nufus'].values
    nufus_data = nufus_data.reshape((-1,1)) #ham veriler
    nufust_data = dft['Nufus'].values
    nufust_data = nufust_data.reshape((-1,1)) #tahmin veriler

    split_percent = 0.70
    split = int(split_percent*len(nufus_data))

    nufus_train = nufus_data[:split]
    nufus_trainx = nufus_train.reshape(-1) #train data
    nufus_test = nufus_data[split-1:]
    nufus_testx = nufus_test.reshape(-1) #kontrol data
    date_train = Tarih[:split] #train tarih
    date_test = Tarih[split-1:] #test tarih

    nufust_pre = nufust_data[40:yil-1978]
    nufust_prex = nufust_pre.reshape(-1) #tahmin data

    nufust_pre_test = nufust_data[split-1:] 
    nufust_pre_testx = nufust_pre_test.reshape(-1) #test data

    pre_yil = np.arange(2020,yil+1,1)
    pre_yil = pd.Series(pre_yil)
    pre_yil.index = pre_yil





fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni5",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
     dcc.Dropdown(id="slct_year_yeni5_1",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
    

    dcc.Graph(id='pred_nufus1'), 
       
])



@app.callback(
    Output('pred_nufus1', 'figure'),
    [Input("slct_year_yeni5", "value")]
)
def display1(value):
    hesap()
    trace1 = go.Scatter(
    x = date_train,
    y = nufus_trainx,
    mode = 'lines',
    name = 'Eğitim Verileri'
)
    trace2 = go.Scatter(
    x = date_test,
    y = nufust_pre_testx,
    mode = 'lines',
    name = 'Test Verileri'
)
    trace3 = go.Scatter(
    x = date_test,
    y = nufus_testx,
    mode='lines',
    name = 'Kontrol Verileri'
)
    trace4 = go.Scatter(
    x = pre_yil,
    y = nufust_prex,
    mode='lines',
    name = 'Tahmin Verileri'
)

    
    layout = go.Layout(
    title = "Nüfus Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "Nüfus"}
)


    fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
   
   
    fig.update_layout({
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig



# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter