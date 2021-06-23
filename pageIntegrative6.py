import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


df_card2 = pd.read_excel('veri2ham.xlsx',  sheet_name='Sheet1')
mevcut_card2 = df_card2.KuruluG*df_card2.YisOlusturma #istihdam
mevcut_card2.index = df_card2.x 
verimlilik_card2 = np.array([5.57, 2.19, 3.12, 4.04, 0.04, 7.83, 3.41]) #uretim/kurulugüç
uretim_card2= 401070.357-290446.924 #ihtiyaç olacak elektrik üretimi
kuruluguc_card2 = uretim_card2/verimlilik_card2 #ihtiyaç olacak kurulu güç
pre_card2 = (kuruluguc_card2*df_card2.YisOlusturma)/10 #gerekli olacak istihdam
pre_card2.index = df_card2.x 
B = np.array([0.14836690050102408, 0.12445634863440393, 0.11705341989131955, 0.14570384986781632,
     0.10783025242823203, 0.15071984795678162, 0.20586938072042246]) #oransal

x = pre_card2.index
y = np.array(kuruluguc_card2)
y = y.astype(int)
y1 = df_card2.KuruluG
# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(name='Mevcut', x=x, y=y1, marker_color='rgb(55, 83, 109)'),
                      go.Bar(name='İhtiyaç', x=x, y=y, marker_color='rgb(26, 118, 255)')])
# Customize aspect
# fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
#                   marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='İhtiyacın Tek Santral Türüne Göre Karşılanması Durumunda Gereken Kurulu Güç')
fig.update_layout({
    
    
    "font_color":"white",
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
})


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter