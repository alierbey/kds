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
pio.templates.default = "seaborn"
import style
import dataGlobals



mevcut_ithal_o = 0
mevcut_yerli_o = 0
ithal_o_son = 0
yerli_o_son = 0


def hesap():
    sy = dataGlobals.seciliTarih #seçillen yıl bilgisi
    # w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1]) #hesaplanan ağırlıklar
    w_son = dataGlobals.w_son

    df = pd.read_excel("veri2.xlsx")
    mevcut = np.array(df.t1) #kaynaklara göre dağılım (mevcut durum)
    t_mevcut = sum(mevcut) #mevcut üretim toplamı
    o_mevcut = np.array(mevcut/t_mevcut)
    yerli_komur_orani = 0.5818
    ithal_komur_orani = 1 - yerli_komur_orani
    ithal_uretim = mevcut[0]*ithal_komur_orani 

    mevcut_ithal_top = ithal_uretim + mevcut[1] #ithal kömür + doğalgaz
    mevcut_yerli_top = t_mevcut - mevcut_ithal_top
    global mevcut_ithal_o
    global mevcut_yerli_o
    mevcut_ithal_o = (mevcut_ithal_top/t_mevcut)*100
    mevcut_yerli_o = (mevcut_yerli_top/t_mevcut)*100

    
    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    deger = round(a*sy*sy+b*sy+c)
    t_ihtiyac = deger - t_mevcut 
    ihtiyac = t_ihtiyac*w_son #kaynaklara göre dağılım (eklenen kısım)
    tum = mevcut + ihtiyac #kaynaklara göre dağılım (son durum)
    t_tum = sum(tum)
    ithal_uretim_son = tum[0]*ithal_komur_orani 
    ithal_top_son = ithal_uretim_son + tum[1] #ithal kömür + doğalgaz
    yerli_top_son = t_tum - ithal_top_son
    global ithal_o_son
    global yerli_o_son
    ithal_o_son = (ithal_top_son/t_tum)*100
    yerli_o_son = (yerli_top_son/t_tum)*100



# fig = go.Figure(layout = go.Layout(
#     title = "Elektrik Üretiminde Yerli Kaynak Kullanım Oranı", title_x=0.5,
# ))

# fig.add_trace(go.Indicator(
#     mode = "number+gauge", value = mevcut_yerli_o, #Son değer
#     domain = {'x': [0.2, 1], 'y': [0.1, 0.4]},
#     title = {"text": "2020"},
#     gauge = {
#         'shape': "bullet",
#         'axis': {'range': [None, 100]}, #toplam uzunluk
#         'steps': [
#             {'range': [0, 50], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
#             ],
#         'bar': {'color': "red"}}))

# fig.add_trace(go.Indicator(
#     mode = "number+gauge", value = yerli_o_son, #Son değer
#     domain = {'x': [0.2, 1], 'y': [0.5, 0.8]},
#     title = {'text': " " +str(sy)+""},
#     gauge = {
#         'shape': "bullet",
#         'axis': {'range': [None, 100]}, #toplam uzunluk
#         'steps': [
#             {'range': [0, 50], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
#             ],
#         'bar': {'color': "blue"}}))


#fig.update_layout(height = 300 , margin = {'t':0, 'b':0, 'l':0})
# fig.update_layout(title_text="Elektrik Üretiminde Yerli Kaynak Kullanım Oranı")


fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni3",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
    html.H6("Kişibaşı Elektrik Tüketim Raporu", style={'text-align': 'center'}),
    dcc.Graph(id='prs_gauge4')
])

@app.callback(
    Output('prs_gauge4', 'figure'),
    [Input("slct_year_yeni3", "value")]
)
def display(value):
    hesap()
    print("****Girdim7****")
    fig = go.Figure(go.Indicator(
    mode = "number+gauge", value = yerli_o_son, #Son değer
    domain = {'x': [0.2, 1], 'y': [0.5, 0.8]},
    title = {'text': " " +str(dataGlobals.seciliTarih)+""},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 100]}, #toplam uzunluk
        'steps': [
            {'range': [0, 50], 'color': "lightgray"}, #Mevcut miktar 150 yerine girilecek
            ],
        'bar': {'color': "blue"}}))
    fig.update_layout({
        "height": 300,
        "font_color":"white",
        "title_font_family":"Times New Roman",
        "title_font_color":"red",
        "legend_title_font_color":"green",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
    return fig


# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter