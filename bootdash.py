import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
from scipy import stats
import scipy as sp
import random
import pageHome
import pageAvailableData
import pageAddingData
import pageDataUpload
import pageDescriptive
import pagePredictive
import pageEnergyMixData
import pageConsumptionForecast
import pageDecision
import pagePrescriptive
import pageIntegrative
import sidebar

# pio.templates.default = "plotly_dark"


# app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
# app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.DARKLY])
# server = app.server

from app import app

import pageConsumptionData



CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
    "background-color": "#161825",
}

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([
    dcc.Location(id="url", refresh=False), 
    sidebar.sidebar, 
    content
])

############################## PAGES #####################

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return pageHome.pageHome
    elif pathname == "/page-1":
        return pageAvailableData.pageAvailableData
    elif pathname == "/page-2":
            return pageAddingData.pageAddingData
    elif pathname == "/page-3":
            return pageDataUpload.pageDataUpload
    elif pathname == "/page-4":
            return pageConsumptionData.pageConsumptionData
    elif pathname == "/page-5":
            return pageEnergyMixData.pageEnergyMixData
    elif pathname == "/page-6":
            return pageConsumptionForecast.pageConsumptionForecast
    elif pathname == "/page-7":
            return pageDecision.pageDecision
    elif pathname == "/page-8":
            return pageDescriptive.pageDescriptive
    elif pathname == "/page-9":
            return pagePredictive.pagePredictive
    elif pathname == "/page-10":
            return pagePrescriptive.pageScriptive
    elif pathname == "/page-11":
            return pageIntegrative.pageIntegrative
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    #app.run_server(debug=True)
    #app.run_server(host='127.0.0.1')
    app.run_server(host='157.230.12.66')

