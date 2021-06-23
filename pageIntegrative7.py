import plotly.graph_objects as go
import numpy as np
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


df_gauge4 = pd.read_excel('veri4.xlsx',  sheet_name='Sheet1') #yerli kaynak kullanım oranı


A = np.array([113117.820, 56702.690, 88886.240, 29672.900, 240.900, 11363.200, 5257.630]) #ham
B = np.array([0.14836690050102408, 0.12445634863440393, 0.11705341989131955, 0.14570384986781632,
     0.10783025242823203, 0.15071984795678162, 0.20586938072042246]) #oransal


mevcut = 290446.2391
son = 401070.357
ihtiyac = son-mevcut
Yeni = ihtiyac*B
# Yeni = np.array([16416.183141990663, 13770.579593335323, 12951.47618399544, 16121.527617318358,
        # 11930.970898032086, 16676.527034238584, 22778.594456189573])
valueR = Yeni + A

fig = go.Figure(layout = go.Layout(
    title = "Elektrik Üretiminde Yerli Kaynak Kullanım Oranı", title_x=0.5,
))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 57.31648, #Son değer
    domain = {'x': [0.2, 1], 'y': [0.1, 0.4]},
    title = {"text": "2019"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 100]}, #toplam uzunluk
        'steps': [
            {'range': [0, 50], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "red"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge", value = 63.31648, #Son değer
    domain = {'x': [0.2, 1], 'y': [0.5, 0.8]},
    title = {'text': "2030"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 100]}, #toplam uzunluk
        'steps': [
            {'range': [0, 50], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))


#fig.update_layout(height = 300 , margin = {'t':0, 'b':0, 'l':0})
fig.update_layout(title_text="Elektrik Üretiminde Yerli Kaynak Kullanım Oranı")
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