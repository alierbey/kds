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



def hesap():
    sy = dataGlobal.seciliTarih #seçillen yıl bilgisi
    a = 152.9413124	
    b = -605364.8062825	
    c = 599056496.6763530
    return round(a*sy*sy+b*sy+c)







fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
    
    html.H6("Tüketimde Beklenen Değişim ", style = {"padding-top":20, "text-align":"center"}),
    dcc.Graph(id='prs_card1')
])

#print(df_tarih.groups.keys())
#print(df_tarih.get_group(1986).Tuketim/df_tarih.get_group(1986).Nufus)

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output('prs_card1', 'figure'),
    [Input("slct_year_yeni", "value")]
)
def display(value):
    
    fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = hesap(),
    title = {"text": "2020 : 259511 GWh</br> </br>" +str(dataGlobal.seciliTarih)+ " : " +str(hesap())+ " GWh"},
    delta = {'reference': 259511, 'relative': True, 'valueformat':',.3%' },
    domain = {'x': [0, 1], 'y': [0, 1]})) 
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