###################### PRESCRIPTIVE graf-3 ######################
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import plotly.io as pio
import sc3
import sc2
import sc1
from app import app
import sc_card1
import sc_card2
import sc_card3



import style

pageIntegrative = html.Div(
    [
        html.H3("Senaryolar"),
        html.Hr(),
        html.Div([
             html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        sc1.fig
                     
                        # dcc.Graph(figure=sc1.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-8",),
             html.Div([
                 
                html.Div([
                    html.Div([
                     sc_card1.fig
                     
                        # dcc.Graph(figure=sc1.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
               ],className="row"),
            html.Hr(),
            html.Div([
            html.Div([
                html.Div([
                    html.Div([
                    #   dcc.Graph(figure=sc2.fig)
                    sc2.fig

                        
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-8",),
            html.Div([
                 
                html.Div([
                    html.Div([
                     sc_card2.fig
                     
                        # dcc.Graph(figure=sc1.fig)
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
               ],className="row"),
            html.Hr(),
            html.Div([
             html.Div([
                html.Div([
                    html.Div([
                            #    dcc.Graph(figure=sc3.fig)
                               sc3.fig
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],
            'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-8",),
                   html.Div([
                 
                html.Div([
                    html.Div([
                     sc_card3.fig
                    ])
                ],style = {'background-color' : style.cardBackColor['back'],'box-shadow': '2px 5px 5px 1px rgba(30, 47, 123, .5)'})            
            ],className="col-xl-4",),
        ],className="row"),       
      
        ],className="row"),
       
       
    ], 
)
