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



tum = 0
t_tum = 0 
mevcut = 0

def hesap():
    
    sy = dataGlobals.seciliTarih
    # w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1]) #hesaplanan ağırlıklar
    w_son = dataGlobals.w_son

    df = pd.read_excel("veri2.xlsx")
    global mevcut
    mevcut = np.array(df.t1) #kaynaklara göre dağılım (mevcut durum)
    t_mevcut = sum(mevcut) #mevcut üretim toplamı
    o_mevcut = np.array(mevcut/t_mevcut)


    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    deger = round(a*sy*sy+b*sy+c)
    t_ihtiyac = deger - t_mevcut 
    ihtiyac = t_ihtiyac*w_son #kaynaklara göre dağılım (eklenen kısım)
    
    global tum
    global t_tum
    tum = mevcut + ihtiyac #kaynaklara göre dağılım (son durum)
    t_tum = sum(tum)



yeni_labels = ['Kömür','Doğalgaz','Hidro','Rüzgâr','Güneş','Jeotermal','Biyokütle']

# fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
# fig.add_trace(go.Pie(labels=labels, values=mevcut, name="2020 Üretim"),
#               1, 1)
# fig.add_trace(go.Pie(labels=labels, values=tum, name= "" +str(sy)+ " Üretim"),
            #   1, 2)

# Use `hole` to create a donut-like pie chart
# fig.update_traces(hole=.4, hoverinfo="label+percent+name")

# fig.update_layout(
#     title_text="Enerji Kaynaklarına Göre Elektrik Üretimi 2020 - " +str(sy)+ "",
#     # Add annotations in the center of the donut pies.
#     annotations=[dict(text='2020', x=0.18, y=0.5, font_size=15, showarrow=False),
#                  dict(text='' +str(sy)+ '', x=0.82, y=0.5, font_size=15, showarrow=False)])


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
    
     html.H6("Kişibaşı Elektrik Tüketim Raporu", style = {"padding":20, "text-align":"center"}),
   
            html.Div([
                html.Div([
                    html.Div([
                         dcc.Graph(id='prs_pie2'), 
                        #  html.A("İleri" , href="/page-4",style={"font-size":18, "font-weight": "bold",'padding':"3rem"}),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-6"),

                html.Div([
                    html.Div([         
                         dcc.Graph(id='prs_pie2_1')
                        #  html.A("İleri" , href="/page-4",style={"font-size":18, "font-weight": "bold",'padding':"3rem"}),
                    ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)',"vertical-align":"middle"})            
                ],className="col-xl-6"),
            ],className="row")
])



@app.callback(
    Output('prs_pie2', 'figure'),
    [Input("slct_year_yeni5", "value")]
)
def display1(value):
    hesap()
    fig = go.Figure(go.Pie(labels=yeni_labels, values=mevcut, name="2020 Üretim"))
    # fig = go.Figure(go.Pie(labels=yeni_labels, values=tum, name= "" +str(dataGlobals.seciliTarih)+ " Üretim"), 1, 2)
    # fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig.update_layout(title_text="Enerji Kaynaklarına Göre Elektrik Üretimi 2020 - " +str(dataGlobals.seciliTarih)+ "", annotations=[ dict(text='' +str(2020)+ '', x=0.5, y=0.5, font_size=12, showarrow=False)])
    fig.update_layout({
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig

@app.callback(
    Output('prs_pie2_1', 'figure'),
    [Input("slct_year_yeni5_1", "value")]
)
def display1(value):
    hesap()
    fig = go.Figure(go.Pie(labels=yeni_labels, values=tum, name= "" +str(dataGlobals.seciliTarih)+ " Üretim"))
    # fig = go.Figure(go.Pie(labels=yeni_labels, values=tum, name= "" +str(dataGlobals.seciliTarih)+ " Üretim"), 1, 2)
    # fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig.update_layout(title_text="Enerji Kaynaklarına Göre Elektrik Üretimi 2020 - " +str(dataGlobals.seciliTarih)+ "", annotations=[ dict(text='' +str(dataGlobals.seciliTarih)+ '', x=0.5, y=0.5, font_size=12, showarrow=False)])
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
