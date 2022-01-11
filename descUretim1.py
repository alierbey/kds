''' Descriptive Üretim Bazlı Mevcut Enerji Çeşitliliği  '''

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


#mevcut üretim (Kömür, Doğalgaz, Hidro, Güneş, Rüzgar, Jeotermal, Biyokütle)
mevcut = np.array([104154.283, 69307.467, 78084.435, 24591.438, 420.223, 9884.549, 5132.992])


'''ENTROPI Hesapla'''
mevcut_oranE = mevcut/sum(mevcut)    
mevcut_oranElog = [math.log(i) for i in mevcut_oranE]
mevcut_oranP = mevcut_oranE*mevcut_oranElog
entropi = (-1/math.log(7))*sum(mevcut_oranP)

fig = go.Figure(layout = go.Layout(
    title = "Senaryo 1 - Enerji Çeşitliliği", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = entropi,
    title = {"text": "2040 Entropi {} <br>2020 Entropi {}".format(round(entropi,5), round(entropi,5))},
    delta = {'reference': entropi, 'relative': True},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig.update_layout(paper_bgcolor = "midnightblue")

fig.update_layout(
    title_text="Üretim Bazlı Mevcut Enerji Çeşitliliği")
 

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
