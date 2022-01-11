# -*- coding: utf-8 -*-
"""
-	Bir pasta grafik yardımıyla elektrik üretiminde mevcut karma verilecek. 
“Mevut Enerji Çeşitliliği (Kurulu GÜç Bazlı)”  başlığı yer alacak. veri2.xlsx 
(Bu ve önceki grafik (desc_card2) yan yana olmalı. 
"""
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

KuruluG = np.array([20322.6, 25674.9, 30983.9, 8832.4, 6667.4, 1613.2, 1484.7])

labels = ['Kömür','Doğalgaz','Hidro','Rüzgâr','Güneş','Jeotermal','Biyokütle']

fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=KuruluG, name="2020 Kurulu Güç"),
              1, 1)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="2020 Kurulu Güç Bazlı Kaynak Çeşitlilği",
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
