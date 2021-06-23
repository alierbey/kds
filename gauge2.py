# Yıllık elektrik tüketim artış hızı

import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.io as pio
from app import app
# pio.templates.default = "plotly_dark"
pio.templates.default = "seaborn"
import style


# app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
df = pd.read_excel("veri1.xlsx")

df['Tarih']=df['Tarih'].dt.year

df_tarih = df.groupby('Tarih').sum()

dff = df_tarih
dff.drop(columns=['SUE','Nufus', 'GSD', 'GSTL', 'GSDp', 'GSTLp', 'kbTuketim'], inplace=True)
# df.reset_index(inplace=True)
# print(df[:5])

a = []
for i in range(len(dff)-1):
    a.append((dff.iloc[i+1,0]-dff.iloc[i,0])*100/dff.iloc[i,0])

    
df_tarih.drop([1986], axis=0, inplace=True) 
a = pd.DataFrame(a, columns=['Oran'] )
a.index = df_tarih.index
a = a.T
b = a.loc["Oran"]


# ------------------------------------------------------------------------------
# App layout
#app.layout = html.Div([
gauge2 = html.Div([
    dcc.Dropdown(id="slct_year_gauge2",
                 options=[{"label": x, "value": x} 
                          for x, row in df_tarih.iterrows()],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'width': "40%","font_color":style.cardBackColor['back'],"padding-left":60},
    ),
    dcc.Graph(id="map")
])

@app.callback(
     Output("map", "figure"), 
    [Input("slct_year_gauge2", "value")])
def display(value):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = b.loc[value],
    #value = 200,
    domain = {'x': [0, 1], 'y': [0, 1]},
   
    
    gauge = {
        'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        }))
    
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

# app.run_server(debug=True)