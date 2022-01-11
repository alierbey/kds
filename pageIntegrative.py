###################### PRESCRIPTIVE graf-3 ######################
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import plotly.io as pio
import sc3
import sc2
import sc1
from app import app



import style

pageIntegrative = html.Div(
    [
        html.H3("Integrative"),
        html.Hr(),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                     
                        dcc.Graph(figure=sc1.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-12",),
            html.Hr(),
            html.Div([
                html.Div([
                    html.Div([
                    #   dcc.Graph(figure=sc2.fig)
                    sc2.fig

                        
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-12",),
            html.Hr(),
             html.Div([
                html.Div([
                    html.Div([
                               dcc.Graph(figure=sc3.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-12",)
        ],className="row"),
        html.Hr(),   
       
    ], 
)
