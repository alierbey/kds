# -*- coding: utf-8 -*-
"""
-	Bir pasta grafik yardımıyla elektrik üretiminde mevcut karma verilecek. 
“Mevut Enerji Çeşitliliği (Üretim Bazlı)”  başlığı yer alacak. veri2.xlsx 
(Bu ve önceki grafik (desc_card1) yan yana olmalı. 
"""
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


df = pd.read_excel("veri2.xlsx")
mevcut = np.array(df.t1) #kaynaklara göre dağılım (mevcut durum)
t_mevcut = sum(mevcut) #mevcut üretim toplamı
o_mevcut = np.array(mevcut/t_mevcut)

labels = ['Kömür','Doğalgaz','Hidro','Rüzgâr','Güneş','Jeotermal','Biyokütle']

fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=mevcut, name="2020 Üretim"),
              1, 1)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="2020 Üretim Bazlı Kaynak Çeşitlilği",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='2020', x=0.5, y=0.5, font_size=15, showarrow=False),
                 ])
fig.update_layout({
    "font_size":12,
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
