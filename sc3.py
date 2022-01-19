''' Scenario Analysis 3  '''

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


mevcut_ilk = 0
mevcut = 0
mevcutkg_ilk = 0
mevcutkg_son = 0 

def hesap():


    global mevcut_ilk
    global mevcut
    global mevcutkg_ilk
    global mevcutkg_son


    e_height = 0
    e_weight = 0

    ihtiyac = 301907
    kademe = 10000
    mevcut_entropi = 0.753327
    # degisim_x = 0.1
    degisim_x = dataGlobals.goalSeekingVeri3
    mdegisim_x = 0.2877
    degisim_o = (3*mdegisim_x)/degisim_x

    # hedef_oran = np.array([0.142857, 0.142857, 0.142857, 0.142857, 0.142857, 0.142857, 0.142857])
    hedef_oran = dataGlobals.w_son
    mevcut = np.array([104154.283, 69307.467, 78084.435, 24591.438, 420.223, 9884.549, 5132.992])
    mevcut_ilk = mevcut

    for i in range(20):
        mevcutT = np.array(sum(mevcut))
        mevcut_oran = mevcut/mevcutT
        katsayilar = hedef_oran/mevcut_oran
        katsayilar_oran = katsayilar/(degisim_o*sum(katsayilar))
        ihtiyac_adim = katsayilar_oran*kademe
        mevcut = mevcut + ihtiyac_adim

    '''ENTROPI Hesapla'''
    mevcut_oranE = mevcut/sum(mevcut)    
    mevcut_oranElog = [math.log(i) for i in mevcut_oranE]
    mevcut_oranP = mevcut_oranE*mevcut_oranElog
    entropi = (-1/math.log(7))*sum(mevcut_oranP)


    entropi_degisim = (entropi - mevcut_entropi)/mevcut_entropi

    kguc_o = [5.12504714, 2.699424996, 2.52016159, 2.78423057, 0.063026534, 6.127292828, 3.457258968]
    mevcutkg_ilk = mevcut_ilk/kguc_o
    mevcutkg_son = mevcut/kguc_o
    #mevcut verisi toplam üretim oranlarını göstermektedir.
    #mevcutkg
    #mevcut ve mevcutkg verileri iki daire grafik halinde sunulacak.





fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni65",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
     dcc.Dropdown(id="slct_year_yeni65_1",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
    

    dcc.Graph(id='pred_sc3'), 
       
])



@app.callback(
    Output('pred_sc3', 'figure'),
    [Input("slct_year_yeni65", "value")]
)
def display1(value):
    hesap()
    labels = ['Kömür','Doğalgaz','Hidro','Rüzgâr','Günes','Jeotermal','Biyokütle']


    fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}], 
                                            [{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=mevcut_ilk, name="2020 Üretim"),
                1, 1)
    fig.add_trace(go.Pie(labels=labels, values=mevcut, name="2040 Üretim"),
                1, 2)
    fig.add_trace(go.Pie(labels=labels, values=mevcutkg_ilk, name="2020 Kurulu Güç"),
                2, 1)
    fig.add_trace(go.Pie(labels=labels, values=mevcutkg_son, name="2040 Kurulu Güç"),
                2, 2)
    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.6, hoverinfo="label+percent+name")

    fig.update_layout(height=700, width=950,
        title_text="Santrallere Göre Elektrik Üretimi 2020-2040",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='2020 <br>Üretim', x=0.17, y=0.83, font_size=15, showarrow=False, 
                        font=dict(size=14, color="#ffffff")),
                    dict(text='2040 <br>Üretim', x=0.83, y=0.83, font_size=15, showarrow=False, 
                        font=dict(size=14, color="#ffffff")),
                    dict(text='2020 <br>Kurulu Güç', x=0.15, y=0.15, font_size=15, showarrow=False, 
                        font=dict(size=14, color="#ffffff")),
                    dict(text='2040 <br>Kurulu Güç', x=0.85, y=0.15, font_size=15, showarrow=False, 
                        font=dict(size=14, color="#ffffff"))])

    fig.update_layout({
        

        "font_color":"white",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    fig.update_layout(
        # height=800,
        title_text='Senaryo 3', title_x=0.5
    )

    return fig


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter



