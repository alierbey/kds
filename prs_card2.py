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
pio.templates.default = "seaborn"
import style
import dataGlobals





def hesap():
    sy = dataGlobals.seciliTarih #seçillen yıl bilgisi
    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    return round(a*sy*sy+b*sy+c)

# w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1]) #hesaplanan ağırlıklar

#skg = round(sum(kuruluguc)) #kurulugüc toplamı

mist = 0
gist = 0

def yeniHesap():
    global mist
    global gist
    KuruluG = np.array([20322.6, 25674.9, 30983.9, 8832.4, 6667.4, 1613.2, 1484.7])
    YisOlusturma = np.array([5.380, 3.950, 7.800, 8.800, 18.200, 11.100, 13.210])
    verim = np.array([5.13, 2.70, 2.52, 2.78, 0.06, 6.13, 3.46]) #uretim/kurulugüç
    ihtiyac = hesap() - 259511 #ihityaç olacak üretim
    ihtiyac_tur = ihtiyac*dataGlobals.w_son
    m_istihdam = (KuruluG*YisOlusturma)/10 #mevcut istihdam
    kuruluguc = np.array(ihtiyac_tur/verim) #ihtiyaç olacak kurulu güç
    g_istihdam = (kuruluguc*YisOlusturma)/100 #gerekli olacak istihdam
    mist = round(sum(m_istihdam)) #mevcut toplam istihdam
    gist = round(sum(g_istihdam)) #beklenen toplam istihdam

# fig = go.Figure(layout = go.Layout(
#     title = "Yeni Is Olusturma Potansiyeli", title_x=0.5,
# ))

# fig.add_trace(go.Indicator(
#     mode = "number+delta",
#     value = mist+gist,
#     title = {"text": "2020 : " +str(mist)+ " </br> </br> " +str(dataGlobals.seciliTarih)+ " : " +str(gist)+ ""},
    
#     delta = {'reference': mist, 'relative': True},
#     domain = {'x': [0, 1], 'y': [0, 1]}))

# fig.update_layout({
#     "height": 300,
#     "font_color":"white",
#     "plot_bgcolor": "rgba(0, 0, 0, 0)",
#     "paper_bgcolor": "rgba(0, 0, 0, 0)",
# })


fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni2",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
    
    html.H6("İstihdam", style = {"padding-top":20, "text-align":"center"}),
    dcc.Graph(id='prs_card2')
])


@app.callback(
    Output('prs_card2', 'figure'),
    [Input("slct_year_yeni2", "value")]
)
def display(value):
    yeniHesap()
    print("****Girdim3****")
    fig = go.Figure(go.Indicator(
     mode = "number+delta",
    value = mist+gist,
    title = {"text": "2020 : " +str(mist)+ " </br> </br> " +str(dataGlobals.seciliTarih)+ " : " +str(gist)+ ""},
    
    delta = {'reference': mist, 'relative': True},
    domain = {'x': [0, 1], 'y': [0, 1]}))
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