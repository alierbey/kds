import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
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

ihtiyac_kg = 0 
mevcut_kg = 0 

def hesap():
    global ihtiyac_kg
    global mevcut_kg
    sy = dataGlobals.seciliTarih  #seçillen yıl bilgisi
    # w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1]) #hesaplanan ağırlıklar
    w_son = dataGlobals.w_son

    df = pd.read_excel("veri2.xlsx")
    mevcut = np.array(df.t1) #kaynaklara göre dağılım (mevcut durum)
    t_mevcut = sum(mevcut) #mevcut üretim toplamı
    o_mevcut = np.array(mevcut/t_mevcut)
    mevcut_kg = np.array(df.t2) #mevcut kurulu güç
    verim = np.array([5.13, 2.70, 2.52, 2.78, 0.06, 6.13, 3.46]) #uretim/kurulugüç

    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    deger = round(a*sy*sy+b*sy+c)
    t_ihtiyac = deger - t_mevcut 
    ihtiyac_kg = np.array(t_ihtiyac/verim)
    ihtiyac = t_ihtiyac*w_son #kaynaklara göre dağılım (eklenen kısım)

yesyeni_labels = ['Kömür','Doğalgaz','Hidro','Rüzgâr','Güneş','Jeotermal','Biyokütle']

# Use the hovertext kw argument for hover text
# fig = go.Figure(data=[go.Bar(name='Mevcut', x=labels, y=mevcut_kg, marker_color='rgb(55, 83, 109)'),
#                       go.Bar(name='İhtiyaç', x=labels, y=ihtiyac_kg, marker_color='rgb(26, 118, 255)')])
# Customize aspect
# fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
#                   marker_line_width=1.5, opacity=0.6)
# fig.update_layout(title_text='İhtiyacın Tek Santral Türüne Göre Karşılanması Durumunda Gereken Kurulu Güç')




fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni6",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
    
    
    html.H6("İhtiyacın Tek Santral Türüne Göre Karşılanması Durumunda Gereken Kurulu Güç", style = {"padding":20, "text-align":"center"}),
    dcc.Graph(id='prs_bar4'),
    
])





@app.callback(
    Output('prs_bar4', 'figure'),
    [Input("slct_year_yeni6", "value")]
)
def display(value):
    hesap()
    print("****Girdim1****")
    fig = go.Figure(data=[go.Bar(name='Mevcut', x=yesyeni_labels, y=mevcut_kg, marker_color='rgb(55, 83, 109)'), go.Bar(name='İhtiyaç', x=yesyeni_labels, y=ihtiyac_kg, marker_color='rgb(26, 118, 255)')])
    fig.update_layout({
        
        "height": 400,
        "font_color":"white",
        "title_font_family":"Times New Roman",
        "title_font_color":"red",
        "legend_title_font_color":"green",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
    return fig


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter