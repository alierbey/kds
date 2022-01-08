''' Scenario Analysis 1  '''

import numpy as np
import pandas as pd
import math
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

####ist_db senaryo1 den, 
#baslangic_w'de ağırlıklardan alınacak. Ağırlıklardan alınan değer yerli ve ithal olarak bölünecek.
#it_oran=0.554625
#y_oran=1-it_oran
#w hesaplanan ağırlıklar olmak üzere
#baslangic_w = [w[0]*it_oran, w[1], w[0]*y_oran, w[2], w[3], w[4], w[5], w[6]]
#aşağıdaki baslangic_w satırını kapat!!!


ist_db = 0.1 #istenen dısa bağımlılık
ihtiyac = 301907 #2040 yılına kadar ihtiyac duyulacak üretim

#mevcut üretim (İthalkömür, Doğalgaz, Yerli kömür, Hidro, Güneş, Rüzgar, Jeotermal, Biyokütle)
mevcut = np.array([57731.927, 69307.467, 46360.487, 78084.435, 24591.438, 420.223, 9884.549, 5132.992])
#baslangic_w değerleri analitik sayfasından hesaplanan ağırlıklar gelecek. 
#Orada hesaplanan ağırlıklar bu sayfa için yerli ithal kömür seçeneği oluşturulmalı
#
baslangic_w = np.array([0.079232, 0.142857143,	0.063625,	0.142857143,	0.142857143,	0.142857143,	0.142857143,	0.142857143
])

top_uretim = ihtiyac + sum(mevcut) #2040 yılında beklenen toplam üretim
ist_ithal = top_uretim * ist_db #dışa bağımlılığa bağlı toplam istenen ithal üretim
ist_yerli = top_uretim - ist_ithal #dışa bağımlılığa bağlı toplam istenen yerli üretim 
yerliWtoplam = sum(baslangic_w[2:]) #yerli ağırlık toplam
ithalWtoplam = sum(baslangic_w) - yerliWtoplam #ithal ağırlık toplam
oran = [baslangic_w[0]/ithalWtoplam, baslangic_w[1]/ithalWtoplam, 
        baslangic_w[2]/yerliWtoplam, baslangic_w[3]/yerliWtoplam, baslangic_w[4]/yerliWtoplam,
        baslangic_w[5]/yerliWtoplam, baslangic_w[6]/yerliWtoplam, baslangic_w[7]/yerliWtoplam]

beklenen_uretim = [oran[0]*ist_ithal, oran[1]*ist_ithal, oran[2]*ist_yerli,
                   oran[3]*ist_yerli, oran[4]*ist_yerli, oran[5]*ist_yerli,
                   oran[6]*ist_yerli, oran[7]*ist_yerli]

degisim_mik = beklenen_uretim - mevcut
degisim_orani = degisim_mik / mevcut




kguc_o = np.array([5.12504714, 2.699424996, 5.12504714, 2.52016159, 2.78423057, 0.063026534, 6.127292828, 3.457258968])
mevcutkg = mevcut/kguc_o
beklenenkg = beklenen_uretim/kguc_o
#mevcut verisi toplam üretim oranlarını göstermektedir.
#mevcutkg
#mevcut ve mevcutkg verileri iki daire grafik halinde sunulacak.



labels = ['İthal Kömür','Doğalgaz','Yerli Kömür','Hidro','Rüzgâr','Günes','Jeotermal','Biyokütle']


fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
                                           #[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=mevcut, name="2020 Üretim"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=beklenen_uretim, name="2040 Üretim"),
              1, 2)
# fig.add_trace(go.Pie(labels=labels, values=mevcutkg, name="2020 Kurulu Güç"),
#               2, 1)
# fig.add_trace(go.Pie(labels=labels, values=beklenenkg, name="2040 Kurulu Güç"),
#               2, 2)
# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.5, hoverinfo="label+percent+name")

fig.update_layout(height=600, width=800,
    title_text="Santrallere Göre Elektrik Üretimi 2020-2040",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='2020 <br>Üretim', x=0.17, y=0.5, font_size=15, showarrow=False, 
                      font=dict(size=14, color="#000000")),
                 dict(text='2040 <br>Üretim', x=0.83, y=0.5, font_size=15, showarrow=False, 
                      font=dict(size=14, color="#000000"))])
                

fig.update_layout({
    

    "font_color":"black",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})
fig.update_layout(
    # height=800,
    title_text='Senaryo 1', title_x=0.5
)


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

