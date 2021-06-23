import plotly.graph_objects as go
import numpy as np


A = np.array([113117.820, 56702.690, 88886.240, 29672.900, 240.900, 11363.200, 5257.630]) #ham
B = np.array([0.14836690050102408, 0.12445634863440393, 0.11705341989131955, 0.14570384986781632,
     0.10783025242823203, 0.15071984795678162, 0.20586938072042246]) #oransal


mevcut = 290446923.91
son = 32949836.63435+35932290.865+34038540.09565+36045753.326299995+32201520.55695+32258251.7876+32314983.01825+33346955.2489+32428445.47955+32485176.7102+33517148.94085+33573880.1715
ihtiyac = son-mevcut
# Yeni = ihtiyac*B
Yeni = np.array([16416.183141990663, 13770.579593335323, 12951.47618399544, 16121.527617318358,
        11930.970898032086, 16676.527034238584, 22778.594456189573])
valueR = Yeni + A

fig = go.Figure(layout = go.Layout(
    title = "Verimlilik", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 5.57, #Son değer
    domain = {'x': [0.05, 0.20], 'y': [0.50, 0.80]},
    title = {"text": "Komur"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 2.19, #Son değer
    domain = {'x': [0.30, 0.45], 'y': [0.50, 0.80]},
    title = {'text': "Doğalgaz"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 3.12, #Son değer
    domain = {'x': [0.55, 0.70], 'y': [0.50, 0.80]},
    title = {'text': "Hidroelektrik"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 4.04, #Son değer
    domain = {'x': [0.80, 0.95], 'y': [0.50, 0.80]},
    title = {'text': "Rüzgar"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 0.04, #Son değer
    domain = {'x': [0.15, 0.30], 'y': [0.05, 0.35]},
    title = {'text': "Günes"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 7.83,
    domain = {'x': [0.40, 0.55], 'y': [0.05, 0.35]},
    title = {'text': "Jeotermal"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]},
        'steps': [
            {'range': [0, 5], 'color': "lightgray"},
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 3.41,
    domain = {'x': [0.65, 0.80], 'y': [0.05, 0.35]},
    title = {'text' :"Atık vb."},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]},
        'steps': [
            {'range': [0, 5], 'color': "lightgray"},
            ],
        'bar': {'color': "red"}}))
fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

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