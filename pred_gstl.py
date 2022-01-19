# -*- coding: utf-8 -*-
"""
GSTL TL Tahmin
"""
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
 
#kullanıcı tarafından girilen yıl verisi gelecek

date_train = 0
gstl_trainx = 0
date_test = 0
gstlt_pre_testx = 0
gstl_testx = 0
pre_yil = 0
gstlt_prex = 0

def hesap():

    global date_train
    global gstl_trainx
    global date_test
    global gstlt_pre_testx
    global gstl_testx
    global pre_yil
    global gstlt_prex

    yil = dataGlobals.seciliTarih

    # Datayı Yükleyelim
    df = pd.read_excel('veri1.xlsx', 'Sheet1', date_parser=[0])
    dft = pd.read_excel('veri1.xlsx', 'Sheet2', date_parser=[0])
    # print(df.info())

    t = [i for i in range(1980, 2021)]
    Tarih = np.array(t)
    #Tarih sütununun index'e Alınması
    df.index = df.Tarih
    dft.index = dft.Tarih
    df.drop(columns=['Tarih', 'Tuketim', 'Nufus', 'GSD', 'SUE'], inplace=True)
    dft.drop(columns=['Tarih', 'Tuketim', 'Nufus', 'GSD', 'SUE'], inplace=True)

    gstl_data = df['GSTL'].values
    gstl_data = gstl_data.reshape((-1,1)) #ham veriler
    gstlt_data = dft['GSTL'].values
    gstlt_data = gstlt_data.reshape((-1,1)) #tahmin veriler

    split_percent = 0.70
    split = int(split_percent*len(gstl_data))

    gstl_train = gstl_data[:split]
    gstl_trainx = gstl_train.reshape(-1) #train data
    gstl_test = gstl_data[split-1:]
    gstl_testx = gstl_test.reshape(-1) #kontrol data
    date_train = Tarih[:split] #train tarih
    date_test = Tarih[split-1:] #test tarih

    gstlt_pre = gstlt_data[40:yil-1978]
    gstlt_prex = gstlt_pre.reshape(-1) #tahmin data

    gstlt_pre_test = gstlt_data[split-1:] 
    gstlt_pre_testx = gstlt_pre_test.reshape(-1) #test data

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
    

    dcc.Graph(id='pred_gstl1'), 
       
])



@app.callback(
    Output('pred_gstl1', 'figure'),
    [Input("slct_year_yeni5", "value")]
)
def display1(value):
    hesap()
    trace1 = go.Scatter(
    x = date_train,
    y = gstl_trainx,
    mode = 'lines',
    name = 'Eğitim Verileri'
)
    trace2 = go.Scatter(
    x = date_test,
    y = gstlt_pre_testx,
    mode = 'lines',
    name = 'Test Verileri'
)
    trace3 = go.Scatter(
    x = date_test,
    y = gstl_testx,
    mode='lines',
    name = 'Kontrol Verileri'
)
    trace4 = go.Scatter(
    x = pre_yil,
    y = gstlt_prex,
    mode='lines',
    name = 'Tahmin Verileri'
)

    layout = go.Layout(
    title = "GSYİH (Türk Lirası) Tahmini",
    xaxis = {'title' : "Tarih"},
    yaxis = {'title' : "Gsyih TL"}
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