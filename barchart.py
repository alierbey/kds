import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

# app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
df = pd.read_excel("veri1_1.xlsx")

df['Tarih']=df['Tarih'].dt.year
df_tarih = df.groupby('Tarih')

# df.reset_index(inplace=True)
# print(df[:5]) 

# ------------------------------------------------------------------------------
# App layout
grafKisiBasi = html.Div([

    
      html.H6("Kişibaşı Elektrik Tüketim Raporu", style = {"padding":20, "text-align":"center"}),

    dcc.Dropdown(id="slct_year",
                 options=[{"label": x, "value": x} 
                          for x in df_tarih.groups.keys()],
                 clearable=False,
                 multi=False,
                 value=1980,
                 style={'width': "40%"}
                 ),

    dcc.Graph(id='mapps')
])

#print(df_tarih.groups.keys())
#print(df_tarih.get_group(1986).Tuketim/df_tarih.get_group(1986).Nufus)

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output('mapps', 'figure'),
    [Input('slct_year', 'value')]
)

# def update_graph(option_slctd):
#     print(option_slctd)
#     print(type(option_slctd))

def display_time_series(slct_year):
    print(slct_year)
    fig = go.Figure(data=[go.Bar(
            x=df_tarih.get_group(slct_year).Periyot, y=df_tarih.get_group(slct_year).Tuketim,
            textposition='auto',
        )])
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6,)
    fig.update_layout({
        
        "font_color":"white",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    return fig

# app.run_server(debug=True)