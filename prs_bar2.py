import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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

mevcut_istihdam = 0
beklenen_istihdam = 0

def hesap():
    sy = 2040 #seçillen yıl bilgisi
    # w_son = np.array([0.1, 0.05, 0.15, 0.25, 0.05, 0.25, 0.1]) #hesaplanan ağırlıklar
    w_son = dataGlobals.w_son
    df = pd.read_excel("veri2.xlsx")
    mevcut = np.array(df.t1) #kaynaklara göre dağılım (mevcut durum)
    t_mevcut = sum(mevcut) #mevcut üretim toplamı
    o_mevcut = np.array(mevcut/t_mevcut)
    mevcut_kg = np.array(df.t2) #mevcut kurulu güç
    verim = np.array([5.13, 2.70, 2.52, 2.78, 0.06, 6.13, 3.46]) #uretim/kurulugüç
    istihdam_o = np.array(df.e4)/10 #istihdam oranı

    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    deger = round(a*sy*sy+b*sy+c)
    t_ihtiyac = deger - t_mevcut 
    ihtiyac = t_ihtiyac*w_son #kaynaklara göre dağılım (eklenen kısım)
    tum = mevcut + ihtiyac #kaynaklara göre dağılım (son durum)
    t_tum = sum(tum)
    global mevcut_istihdam
    global beklenen_istihdam
    mevcut_istihdam = np.round(mevcut_kg*istihdam_o)
    beklenen_istihdam = ((ihtiyac / verim)*istihdam_o)





labels_bar2 = ['Kömür','Doğalgaz','Hidro','Rüzgâr','Güneş','Jeotermal','Biyokütle']

# # Use the hovertext kw argument for hover text
# fig = go.Figure(data=[go.Bar(x=labels_bar2, y=mevcut_istihdam, name="Mevcut İstihdam"),
#                       go.Bar(x=labels_bar2, y=beklenen_istihdam, name="Potansiyel İstihdam")])
# # Customize aspect
# # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
# #                   marker_line_width=1.5, opacity=0.6)
# fig.update_layout(barmode='group')
# fig.update_layout(title_text='Santral Türlerine Göre İstihdama Katkı')


fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni13",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
    
    dcc.Graph(id='prs_card13')
])



@app.callback(
    Output('prs_card13', 'figure'),
    [Input("slct_year_yeni13", "value")]
)
def display(value):
    hesap()
    print("****Girdim13****")
    fig = go.Figure(data=[go.Bar(x=labels_bar2, y=mevcut_istihdam, name="Mevcut İstihdam"),
                      go.Bar(x=labels_bar2, y=beklenen_istihdam, name="Potansiyel İstihdam")])
    fig.update_layout(barmode='group')
    
    fig.update_layout({
        "height": 420,
        "font_color":"white",
        "title_font_family":"Times New Roman",
        "title_font_color":"red",
        "legend_title_font_color":"green",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
    return fig


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter