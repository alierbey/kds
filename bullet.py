import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
pio.templates.default = "plotly_dark"

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

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 129534, #Son değer
    delta = {'reference': 113117.820}, #Mevcut miktar
    domain = {'x': [0.25, 1], 'y': [0.91, 0.98]},
    title = {'text': "Komur"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]}, #toplam uzunluk
        'steps': [
            {'range': [0, 113117.820], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 70473.3, #Son değer
    delta = {'reference': 56702.690}, #Mevcut miktar
    domain = {'x': [0.25, 1], 'y': [0.77, 0.84]},
    title = {'text': "Doğalgaz"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]}, #toplam uzunluk
        'steps': [
            {'range': [0, 56702.690], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 101838, #Son değer
    delta = {'reference': 88886.240}, #Mevcut miktar
    domain = {'x': [0.25, 1], 'y': [0.36, 0.43]},
    title = {'text': "Hidroelektrik"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]}, #toplam uzunluk
        'steps': [
            {'range': [0, 88886.240], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 45794.4, #Son değer
    delta = {'reference': 29672.900}, #Mevcut miktar
    domain = {'x': [0.25, 1], 'y': [0.50, 0.57]},
    title = {'text': "Rüzgar"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]}, #toplam uzunluk
        'steps': [
            {'range': [0, 29672.900], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 12171.9, #Son değer
    delta = {'reference': 240.900}, #Mevcut miktar
    domain = {'x': [0.25, 1], 'y': [0.64, 0.71]},
    title = {'text': "Günes"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]}, #toplam uzunluk
        'steps': [
            {'range': [0, 240.900], 'color': "gray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 28039.7,
    delta = {'reference': 11363.200},
    domain = {'x': [0.25, 1], 'y': [0.22, 0.29]},
    title = {'text': "Jeotermal"},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]},
        'steps': [
            {'range': [0, 11363.200], 'color': "gray"},
            ],
        'bar': {'color': "blue"}}))

fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = 28036.2,
    delta = {'reference': 5257.630},
    domain = {'x': [0.25, 1], 'y': [0.08, 0.15]},
    title = {'text' :"Atık vb."},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 200000]},
        'steps': [
            {'range': [0, 5257.630], 'color': "gray"},
            ],
        'bar': {'color': "blue"}}))
fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

fig.update_layout({
"font_size":12,
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
})
