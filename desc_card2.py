# -*- coding: utf-8 -*-
"""
-	“Kurlu Güç Bazlı Mevcut Enerji Çeşitliliği” bu başlık için bir kart gösterimi ayarlanacak ve mevcut entropi değerini gösterecek
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np

df = pd.read_excel("veri2.xlsx")
KuruluG = np.array(df.t2) #kurulu gücün kaynaklara göre dağılım (mevcut durum)
t_KuruluG = sum(KuruluG) #mevcut kurluG toplamı
o_KuruluG = np.array(KuruluG/t_KuruluG)

k= -1/np.log(7)
entr_ilk =  k*sum(o_KuruluG*np.log(o_KuruluG))

fig = go.Figure(layout = go.Layout(
    #title = "Kurulu Güç", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number",
    value = entr_ilk,
    title = {"text": "2020 Kurulu Güç Bazlı Entropi Değeri"},
    domain = {'x': [0, 1], 'y': [0, 0.5]}))
    
fig.update_layout({
    "font_size":12,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })

# fig.update_layout(paper_bgcolor = "thistle")

# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
