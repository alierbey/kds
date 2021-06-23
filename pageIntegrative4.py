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
uretim_card2= 355070.357-290446.924 #ihtiyaç olacak elektrik üretimi
kuruluguc_card2 = uretim_card2/verimlilik_card2 #ihtiyaç olacak kurulu güç
pre_card2 = (kuruluguc_card2*df_card2.YisOlusturma)/10 #gerekli olacak istihdam
pre_card2.index = df_card2.x 

x = pre_card2.index
y = np.array(pre_card2/10+mevcut_card2)
y = y.astype(int)
# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(x=x, y=y)])
# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='Santral Türlerine Göre İstihdama Katkı')
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