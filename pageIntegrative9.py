import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math


df = pd.read_excel("veri2ham.xlsx")

# # # print(df_tur.groups.keys())

A = np.array([113117.820, 56702.690, 88886.240, 29672.900, 240.900, 11363.200, 5257.630]) #ham üretim
B = np.array([0.14836690050102408, 0.12445634863440393, 0.11705341989131955, 0.14570384986781632,
     0.10783025242823203, 0.15071984795678162, 0.20586938072042246]) #oransal


mevcut = 290446923.91
son = 32949836.63435+35932290.865+34038540.09565+36045753.326299995+32201520.55695+32258251.7876+32314983.01825+33346955.2489+32428445.47955+32485176.7102+33517148.94085+33573880.1715
ihtiyac = son-mevcut
# Yeni = ihtiyac*B
Yeni = np.array([16416.183141990663, 13770.579593335323, 12951.47618399544, 16121.527617318358,
        11930.970898032086, 16676.527034238584, 22778.594456189573])
valueR = Yeni + A
#print(df_cat('Cevre'))

labels = ['Kömür','Doğalgaz','Hidroelektrik','Rüzgar','Günes','Jeotermal','Atık vb.']
values2019 = np.array(df.Uretim)
values2030 = valueR
nvalues2019 = values2019/values2019.sum()
nvalues2030 = values2030/values2030.sum()
k = 1/7
entropi2019 = -k*sum(nvalues2019*np.log(nvalues2019))
entropi2030 = -k*sum(nvalues2030*np.log(nvalues2030))


fig = go.Figure(layout = go.Layout(
    #title = "Kurulu Güç", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number",
    value = entropi2019,
    title = {"text": "2019 Entropi Değeri"},
    domain = {'x': [0, 1], 'y': [0, 0.5]}))

fig.add_trace(go.Indicator(
    mode = "number",
    value = entropi2030,
    title = {"text": "2030 Entropi Değeri"},
    domain = {'x': [0, 1], 'y': [0.5, 1]}))

fig.update_layout(paper_bgcolor = "thistle")

fig.update_layout({
    

    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})


# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter