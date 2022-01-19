import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.templates.default = "plotly_dark"
import dataGlobals
import pandas as pd
import numpy as np
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
import dataGlobals
from app import app
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import dataGlobals

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
from prs_card2 import yeniHesap
pio.templates.default = "seaborn"
import style
import dataGlobals



agirlik = 0

def hesap():
    global agirlik
    agirlik = dataGlobals.w_ham





fig = html.Div([
    
    dcc.Dropdown(id="slct_year_yeni345",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
    dcc.Dropdown(id="slct_year_yeni345_1",
                 options=[{"label": x, "value": x} 
                          for x in range(2021,2040)],
                 clearable=False,
                 multi=False,
                 value=1987,
                 style={'display':'none','width': "40%","padding-left":60},
    ),
    

    dcc.Graph(id='pres_sunburst_345'), 
       
])



@app.callback(
    Output('pres_sunburst_345', 'figure'),
    [Input("slct_year_yeni345", "value")]
)
def display1(value):
    hesap()
  
    
    kriter = ["CO2", "CO", "NOx", "SO2", "A. Kullanımı", "Y. Maliyeti", 
           "İ. Maliyeti", "Geri Ö. S.", "İstihdam", "Üretim", "Kurulu G.", "İ. Ömrü", "E. Verimliliği", "K. Faktörü"]
    kategori = ["Çevre", "Çevre","Çevre","Çevre","Çevre",
            "Ekonomik","Ekonomik","Ekonomik","Ekonomik","Teknik", "Teknik", "Teknik", "Teknik", "Teknik" ]
    df = pd.DataFrame(
        dict(kriter=kriter, kategori=kategori, agirlik=agirlik)
    )
    # agirlik = [0.193066, 0.175514, 0.152621, 0.127184, 0.101747, 0.0782672, 0.0579757,
    #            0.0414112, 0.0285595, 0.0190397, 0.0122836, 0.00767728, 0.0046529]



    fig = px.sunburst(df, path=['kategori', 'kriter'], values='agirlik')


    fig.update_layout({
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })


    return fig