import plotly.graph_objects as go
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




fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni_sc2",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
    
    html.H6("Senaryo 2 Değişim ", style = {"padding-top":20, "text-align":"center"}),
    dcc.Graph(id='sc_card2')
])

#print(df_tarih.groups.keys())
#print(df_tarih.get_group(1986).Tuketim/df_tarih.get_group(1986).Nufus)

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output('sc_card2', 'figure'),
    [Input("slct_year_yeni_sc2", "value")]
)
def display(value):
    
    sy = dataGlobals.seciliTarih #seçillen yıl bilgisi
    dgr = dataGlobals.goalSeekingVeri2 #goal seeking senaryo 1 için seçilen değer
    dgr = dgr * 100

    fig = go.Figure(layout = go.Layout(
        title = "Elektrik üretimi için kullanılan kaynaklarda <br> 2020 yılı itibariyle<br> yenilenebilir oranı %40,51’dir. " +str(sy)+ " yılında<br> Yenilenebilir kaynak kullanım oranını<br> % " +str(dgr)+ " seviyesine ulaştırabilmek için <br> enerji karmasının yandaki şekilde sunulduğu<br> gibi planlanması gerekmektedir."
    ))

    fig.add_trace(go.Indicator(
        mode = "delta",
        value = dgr,
        delta = {'reference': 40.5, 'relative': True ,'valueformat':',.3%'},
        domain = {'x': [0, 1], 'y': [0, 1]})),


    fig.update_layout({
        "height": 400,
        "font_color":"gray",
        "font_size":11,
        
        "title_font_color":"gray",
        "title_font_size":15,
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
