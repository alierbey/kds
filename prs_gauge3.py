import plotly.graph_objects as go
import numpy as np


verim = np.array([5.13, 2.70, 2.52, 2.78, 0.06, 6.13, 3.46]) #uretim/kurulugüç

fig = go.Figure(layout = go.Layout(
    title = "", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = verim[0], #Son değer
    domain = {'x': [0.05, 0.20], 'y': [0.50, 0.80]},
    title = {"text": "Kömür"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = verim[1], #Son değer
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
    mode = "number+gauge", value = verim[2], #Son değer
    domain = {'x': [0.55, 0.70], 'y': [0.50, 0.80]},
    title = {'text': "Hidro"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = verim[3], #Son değer
    domain = {'x': [0.80, 0.95], 'y': [0.50, 0.80]},
    title = {'text': "Rüzgâr"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = verim[4], #Son değer
    domain = {'x': [0.15, 0.30], 'y': [0.05, 0.35]},
    title = {'text': "Güneş"},
    gauge = {
        'shape': "angular",
        'axis': {'range': [None, 10]}, #toplam uzunluk
        'steps': [
            {'range': [0, 5], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = verim[5],
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
    mode = "number+gauge", value = verim[6],
    domain = {'x': [0.65, 0.80], 'y': [0.05, 0.35]},
    title = {'text' :"Biyokütle"},
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